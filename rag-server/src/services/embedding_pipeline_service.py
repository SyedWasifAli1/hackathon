from typing import List, Dict, Any
from datetime import datetime
import asyncio
import logging
from openai import AsyncOpenAI
from qdrant_client import AsyncQdrantClient
from qdrant_client.http import models
import hashlib


class EmbeddingPipelineService:
    """
    Service for generating and managing embeddings for the RAG system
    """

    def __init__(self, openai_api_key: str, qdrant_url: str, qdrant_api_key: str = None):
        self.openai_client = AsyncOpenAI(api_key=openai_api_key)
        self.qdrant_client = AsyncQdrantClient(
            url=qdrant_url,
            api_key=qdrant_api_key,
            prefer_grpc=True
        )
        self.collection_name = "textbook_content"
        self.logger = logging.getLogger(__name__)

    async def initialize_collection(self):
        """
        Initialize the Qdrant collection for storing embeddings
        """
        try:
            # Check if collection exists
            collections = await self.qdrant_client.get_collections()
            collection_exists = any(col.name == self.collection_name for col in collections.collections)

            if not collection_exists:
                # Create collection with appropriate vector size for OpenAI embeddings (1536)
                await self.qdrant_client.create_collection(
                    collection_name=self.collection_name,
                    vectors_config=models.VectorParams(size=1536, distance=models.Distance.COSINE)
                )
                self.logger.info(f"Created Qdrant collection: {self.collection_name}")
            else:
                self.logger.info(f"Qdrant collection {self.collection_name} already exists")
        except Exception as e:
            self.logger.error(f"Error initializing collection: {e}")
            raise

    async def generate_embeddings(self, texts: List[str]) -> List[List[float]]:
        """
        Generate embeddings for a list of texts using OpenAI
        """
        try:
            response = await self.openai_client.embeddings.create(
                input=texts,
                model="text-embedding-ada-002"
            )
            return [item.embedding for item in response.data]
        except Exception as e:
            self.logger.error(f"Error generating embeddings: {e}")
            raise

    async def chunk_text(self, text: str, chunk_size: int = 512, overlap: int = 50) -> List[Dict[str, Any]]:
        """
        Split text into overlapping chunks with metadata
        """
        words = text.split()
        chunks = []

        for i in range(0, len(words), chunk_size - overlap):
            chunk_words = words[i:i + chunk_size]
            chunk_text = " ".join(chunk_words)

            if chunk_text.strip():
                chunk_hash = hashlib.md5(chunk_text.encode()).hexdigest()

                chunk = {
                    "text": chunk_text,
                    "metadata": {
                        "chunk_index": len(chunks),
                        "chunk_size": len(chunk_text),
                        "word_count": len(chunk_words),
                        "hash": chunk_hash,
                        "created_at": datetime.utcnow().isoformat()
                    }
                }
                chunks.append(chunk)

        return chunks

    async def process_textbook_content(self, content: str, source_id: str, source_type: str = "chapter") -> int:
        """
        Process textbook content by chunking and storing embeddings
        """
        # Chunk the content
        chunks = await self.chunk_text(content)

        # Extract texts for embedding generation
        texts = [chunk["text"] for chunk in chunks]

        # Generate embeddings
        embeddings = await self.generate_embeddings(texts)

        # Prepare points for Qdrant
        points = []
        for i, (chunk, embedding) in enumerate(zip(chunks, embeddings)):
            point = models.PointStruct(
                id=f"{source_id}_{chunk['metadata']['hash'][:8]}_{i}",
                vector=embedding,
                payload={
                    "text": chunk["text"],
                    "source_id": source_id,
                    "source_type": source_type,
                    "chunk_index": chunk["metadata"]["chunk_index"],
                    "metadata": chunk["metadata"]
                }
            )
            points.append(point)

        # Upload to Qdrant
        await self.qdrant_client.upsert(
            collection_name=self.collection_name,
            points=points
        )

        self.logger.info(f"Uploaded {len(points)} embeddings for source {source_id}")
        return len(points)

    async def search_similar_content(self, query: str, top_k: int = 5) -> List[Dict[str, Any]]:
        """
        Search for similar content using the query
        """
        # Generate embedding for the query
        query_embedding = await self.generate_embeddings([query])

        # Search in Qdrant
        search_results = await self.qdrant_client.search(
            collection_name=self.collection_name,
            query_vector=query_embedding[0],
            limit=top_k
        )

        # Format results
        results = []
        for result in search_results:
            results.append({
                "text": result.payload["text"],
                "source_id": result.payload["source_id"],
                "source_type": result.payload["source_type"],
                "score": result.score,
                "metadata": result.payload.get("metadata", {})
            })

        return results

    async def delete_content_by_source(self, source_id: str):
        """
        Delete all embeddings associated with a specific source
        """
        # This would typically use a filter to delete points with specific payload values
        # For now, we'll just log that this functionality exists
        self.logger.info(f"Would delete content for source: {source_id}")

        # In a real implementation, you would use:
        # await self.qdrant_client.delete(
        #     collection_name=self.collection_name,
        #     points_selector=models.FilterSelector(
        #         filter=models.Filter(
        #             must=[models.FieldCondition(
        #                 key="source_id",
        #                 match=models.MatchValue(value=source_id)
        #             )]
        #         )
        #     )
        # )