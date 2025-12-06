from typing import List, Optional
from ..models.rag_query import RAGQuery
from ..models.embedding_chunk import EmbeddingChunk
from uuid import uuid4
from datetime import datetime
import asyncio


class RAGService:
    """
    Service class to handle RAG (Retrieval-Augmented Generation) operations
    """

    def __init__(self):
        # In a real implementation, this would connect to a vector database like Qdrant
        self.queries: List[RAGQuery] = []
        self.chunks: List[EmbeddingChunk] = []

    async def create_query(self, query_data: dict) -> RAGQuery:
        """
        Create a new RAG query
        """
        query = RAGQuery(
            id=str(uuid4()),
            query_text=query_data.get("query_text"),
            context_text=query_data.get("context_text"),
            source_id=query_data.get("source_id"),
            source_type=query_data.get("source_type"),
            user_id=query_data.get("user_id"),
            session_id=query_data.get("session_id"),
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )
        self.queries.append(query)
        return query

    async def get_query_by_id(self, query_id: str) -> Optional[RAGQuery]:
        """
        Retrieve a RAG query by its ID
        """
        for query in self.queries:
            if query.id == query_id:
                return query
        return None

    async def search_chunks(self, query_text: str, top_k: int = 5) -> List[EmbeddingChunk]:
        """
        Search for relevant chunks based on the query text
        In a real implementation, this would use vector similarity search
        """
        # This is a simplified implementation that just returns some chunks
        # In a real system, this would perform vector similarity search
        results = []
        for chunk in self.chunks:
            # Simple text matching for demo purposes
            if query_text.lower() in chunk.content.lower():
                chunk.similarity_score = 0.8  # Simulated similarity score
                results.append(chunk)
            if len(results) >= top_k:
                break

        # If no exact matches, return top chunks
        if not results:
            results = self.chunks[:top_k] if len(self.chunks) > top_k else self.chunks
            for chunk in results:
                chunk.similarity_score = 0.5  # Default score for unmatched chunks

        return results

    async def generate_response(self, query_text: str, context_chunks: List[EmbeddingChunk]) -> str:
        """
        Generate a response based on the query and context chunks
        In a real implementation, this would call an LLM
        """
        # In a real system, this would call an LLM with the context
        context = " ".join([chunk.content for chunk in context_chunks[:3]])  # Use top 3 chunks
        response = f"Based on the textbook content, here's an answer to your question: '{query_text}'. The relevant information is: {context[:200]}..."
        return response

    async def process_query(self, query_data: dict) -> RAGQuery:
        """
        Process a complete RAG query: search, generate response, and store
        """
        # Create the query record
        query = await self.create_query(query_data)

        # Search for relevant chunks
        relevant_chunks = await self.search_chunks(query.query_text)

        # Generate response based on chunks
        response_text = await self.generate_response(query.query_text, relevant_chunks)

        # Update the query with response and retrieved chunks
        query.response_text = response_text
        query.retrieved_chunks = [chunk.content for chunk in relevant_chunks]
        query.updated_at = datetime.utcnow()

        # Update in our in-memory store
        for i, q in enumerate(self.queries):
            if q.id == query.id:
                self.queries[i] = query
                break

        return query

    async def add_embedding_chunk(self, chunk_data: dict) -> EmbeddingChunk:
        """
        Add a new embedding chunk to the system
        """
        chunk = EmbeddingChunk(
            id=str(uuid4()),
            content=chunk_data.get("content"),
            embedding=chunk_data.get("embedding"),
            source_id=chunk_data.get("source_id"),
            source_type=chunk_data.get("source_type"),
            chunk_index=chunk_data.get("chunk_index"),
            metadata=chunk_data.get("metadata", {}),
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )
        self.chunks.append(chunk)
        return chunk

    async def get_chunks_by_source(self, source_id: str, source_type: str) -> List[EmbeddingChunk]:
        """
        Retrieve all chunks for a specific source
        """
        return [
            chunk for chunk in self.chunks
            if chunk.source_id == source_id and chunk.source_type.value == source_type
        ]