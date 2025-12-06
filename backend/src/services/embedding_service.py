from typing import List, Optional
from ..models.embedding_chunk import EmbeddingChunk
from uuid import uuid4
from datetime import datetime
import asyncio


class EmbeddingService:
    """
    Service class to handle embedding operations for the RAG system
    """

    def __init__(self):
        # In a real implementation, this would connect to an embedding model API
        # like OpenAI embeddings or a local model
        pass

    async def create_embeddings(self, texts: List[str]) -> List[List[float]]:
        """
        Create embeddings for a list of texts
        In a real implementation, this would call an embedding model
        """
        # This is a simplified implementation that returns dummy embeddings
        # In a real system, this would call an embedding API like OpenAI
        embeddings = []
        for text in texts:
            # Generate a dummy embedding (in reality, this would be from an ML model)
            # Using a simple hash-based approach for demonstration
            embedding = [hash(f"{text}_{i}") % 1000 / 1000.0 for i in range(1536)]  # 1536-dim like OpenAI
            embeddings.append(embedding)
        return embeddings

    async def chunk_text(self, text: str, chunk_size: int = 512, overlap: int = 50) -> List[str]:
        """
        Split text into overlapping chunks suitable for embedding
        """
        words = text.split()
        chunks = []

        for i in range(0, len(words), chunk_size - overlap):
            chunk_words = words[i:i + chunk_size]
            chunk = " ".join(chunk_words)
            if chunk.strip():
                chunks.append(chunk)

        return chunks

    async def process_document_for_embeddings(self, content: str, source_id: str, source_type: str) -> List[EmbeddingChunk]:
        """
        Process a document to create embedding chunks
        """
        # Chunk the content
        text_chunks = await self.chunk_text(content)

        # Create embeddings for each chunk
        embeddings = await self.create_embeddings(text_chunks)

        # Create embedding chunks
        embedding_chunks = []
        for i, (chunk_text, embedding) in enumerate(zip(text_chunks, embeddings)):
            chunk = EmbeddingChunk(
                id=str(uuid4()),
                content=chunk_text,
                embedding=embedding,
                source_id=source_id,
                source_type=source_type,
                chunk_index=i,
                metadata={
                    "chunk_size": len(chunk_text),
                    "word_count": len(chunk_text.split())
                },
                created_at=datetime.utcnow(),
                updated_at=datetime.utcnow()
            )
            embedding_chunks.append(chunk)

        return embedding_chunks

    async def find_similar_chunks(self, query_embedding: List[float], all_chunks: List[EmbeddingChunk], top_k: int = 5) -> List[EmbeddingChunk]:
        """
        Find the most similar chunks to the query embedding using cosine similarity
        """
        # Calculate similarity scores (simplified cosine similarity)
        scored_chunks = []
        for chunk in all_chunks:
            if chunk.embedding:
                # Calculate dot product (simplified similarity calculation)
                similarity = sum(a * b for a, b in zip(query_embedding, chunk.embedding))
                chunk.similarity_score = similarity
                scored_chunks.append((chunk, similarity))

        # Sort by similarity score and return top_k
        scored_chunks.sort(key=lambda x: x[1], reverse=True)
        return [chunk for chunk, score in scored_chunks[:top_k]]