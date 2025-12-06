from fastapi import APIRouter, HTTPException
from typing import List
from datetime import datetime
from ..models.rag_query import RAGQuery
from ..services.rag_service import RAGService
from ..services.embedding_service import EmbeddingService

router = APIRouter()
rag_service = RAGService()
embedding_service = EmbeddingService()


@router.post("/rag/query", response_model=RAGQuery)
async def query_rag(query_data: dict):
    """
    Process a RAG query and return the response
    """
    try:
        # Process the query through the RAG service
        result = await rag_service.process_query(query_data)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/rag/query/{query_id}", response_model=RAGQuery)
async def get_rag_query(query_id: str):
    """
    Retrieve a specific RAG query by ID
    """
    query = await rag_service.get_query_by_id(query_id)
    if not query:
        raise HTTPException(status_code=404, detail="Query not found")
    return query


@router.post("/rag/process-text")
async def process_text_for_rag(process_data: dict):
    """
    Process text content to prepare it for RAG system
    """
    try:
        content = process_data.get("content", "")
        source_id = process_data.get("source_id", "")
        source_type = process_data.get("source_type", "textbook_chapter")

        # Process the document to create embedding chunks
        embedding_chunks = await embedding_service.process_document_for_embeddings(
            content, source_id, source_type
        )

        # Add the chunks to the RAG service
        for chunk_data in embedding_chunks:
            await rag_service.add_embedding_chunk(chunk_data.dict())

        return {
            "message": f"Successfully processed {len(embedding_chunks)} chunks",
            "chunk_count": len(embedding_chunks)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/rag/feedback/{query_id}")
async def provide_feedback(query_id: str, feedback_data: dict):
    """
    Add feedback to a RAG response
    """
    query = await rag_service.get_query_by_id(query_id)
    if not query:
        raise HTTPException(status_code=404, detail="Query not found")

    # Update the feedback score
    feedback_score = feedback_data.get("feedback_score", 0)
    query.feedback_score = feedback_score
    query.updated_at = datetime.utcnow()

    # In a real implementation, you would update the query in the database
    # For now, we'll just return a success message
    # Update the query in our in-memory store
    for i, q in enumerate(rag_service.queries):
        if q.id == query.id:
            rag_service.queries[i] = query
            break

    return {
        "message": "Feedback recorded successfully",
        "query_id": query_id,
        "feedback_score": query.feedback_score
    }