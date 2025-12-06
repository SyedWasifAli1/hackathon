// API service for RAG (Retrieval-Augmented Generation) functionality

interface RAGQueryRequest {
  query_text: string;
  context_text?: string;
  source_id?: string;
  source_type?: string;
  user_id?: string;
  session_id?: string;
}

interface RAGQueryResponse {
  id: string;
  query_text: string;
  response_text: string;
  retrieved_chunks?: string[];
  confidence_score?: number;
  created_at: string;
}

interface ProcessTextRequest {
  content: string;
  source_id: string;
  source_type: string;
}

interface ProcessTextResponse {
  message: string;
  chunk_count: number;
}

class RAGAPIService {
  private baseUrl: string;

  constructor(baseUrl: string = '/api') {
    this.baseUrl = baseUrl;
  }

  async queryRAG(queryData: RAGQueryRequest): Promise<RAGQueryResponse> {
    try {
      const response = await fetch(`${this.baseUrl}/rag/query`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(queryData),
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const data = await response.json();
      return data;
    } catch (error) {
      console.error('Error querying RAG system:', error);
      throw error;
    }
  }

  async getQueryById(queryId: string): Promise<RAGQueryResponse> {
    try {
      const response = await fetch(`${this.baseUrl}/rag/query/${queryId}`, {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
        },
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const data = await response.json();
      return data;
    } catch (error) {
      console.error('Error fetching RAG query:', error);
      throw error;
    }
  }

  async processTextForRAG(processData: ProcessTextRequest): Promise<ProcessTextResponse> {
    try {
      const response = await fetch(`${this.baseUrl}/rag/process-text`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(processData),
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const data = await response.json();
      return data;
    } catch (error) {
      console.error('Error processing text for RAG:', error);
      throw error;
    }
  }

  async provideFeedback(queryId: string, feedbackScore: number): Promise<{ message: string, query_id: string, feedback_score: number }> {
    try {
      const response = await fetch(`${this.baseUrl}/rag/feedback/${queryId}`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ feedback_score: feedbackScore }),
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const data = await response.json();
      return data;
    } catch (error) {
      console.error('Error providing feedback:', error);
      throw error;
    }
  }
}

export default RAGAPIService;