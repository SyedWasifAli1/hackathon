# Quickstart Guide: Physical AI & Humanoid Robotics Textbook

**Feature**: 001-textbook-spec
**Date**: 2025-12-06

## Overview

This guide provides a quick setup for the Physical AI & Humanoid Robotics textbook platform with integrated RAG chatbot, multilingual support, and interactive learning modules.

## Prerequisites

- Node.js 18+ for Docusaurus frontend
- Python 3.11+ for backend services
- Access to OpenAI API key
- Qdrant Cloud account
- Neon Postgres account
- Better-Auth configuration

## Local Development Setup

### 1. Clone and Initialize Repository

```bash
git clone <repository-url>
cd <repository-name>
```

### 2. Frontend Setup (Docusaurus)

```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Set environment variables
cp .env.example .env
# Edit .env with your API keys and configuration
```

### 3. Backend Setup (FastAPI)

```bash
# Navigate to RAG server directory
cd rag-server

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set environment variables
cp .env.example .env
# Edit .env with your API keys and configuration
```

### 4. Environment Variables

Create `.env` files with the following variables:

**Frontend (.env):**
```
REACT_APP_OPENAI_API_KEY=your_openai_key
REACT_APP_RAG_API_URL=http://localhost:8000
REACT_APP_BETTER_AUTH_URL=http://localhost:4000
```

**Backend (.env):**
```
OPENAI_API_KEY=your_openai_key
QDRANT_URL=your_qdrant_url
QDRANT_API_KEY=your_qdrant_key
DATABASE_URL=your_neon_postgres_url
BETTER_AUTH_URL=your_auth_url
```

## Running the Application

### 1. Start the RAG Backend

```bash
cd rag-server
source venv/bin/activate  # Activate virtual environment
python -m uvicorn src.main:app --reload --port 8000
```

### 2. Start the Frontend

```bash
cd frontend
npm start
```

The application will be available at `http://localhost:3000`

## Key Features Setup

### 1. Content Generation

To generate textbook content using Claude Code:

```bash
# Run content generation script
python scripts/generate-content.py
```

### 2. Embedding Generation

To create embeddings for RAG:

```bash
# Generate embeddings from textbook content
python scripts/build-embeddings.py
```

### 3. Testing the RAG System

```bash
# Test RAG functionality
curl -X POST http://localhost:8000/rag/query \
  -H "Content-Type: application/json" \
  -d '{
    "query": "What is ROS 2?",
    "selected_text": "Robot Operating System 2 is a flexible framework for writing robot applications."
  }'
```

## API Endpoints

### RAG Service
- `POST /rag/query` - Submit queries to the RAG system
- `POST /rag/feedback` - Submit feedback on RAG responses
- `GET /rag/health` - Check service health

### Authentication
- `POST /auth/register` - User registration
- `POST /auth/login` - User login
- `GET /auth/profile` - Get user profile

### Personalization
- `GET /personalization/settings` - Get user settings
- `PUT /personalization/settings` - Update user settings
- `GET /personalization/recommendations` - Get content recommendations

## Deployment

### 1. Frontend Deployment (GitHub Pages)

```bash
# Build the frontend
npm run build

# Deploy to GitHub Pages
npm run deploy
```

### 2. Backend Deployment (Vercel)

```bash
# Deploy using Vercel CLI
vercel --prod
```

## Troubleshooting

### Common Issues

1. **Environment Variables Not Loading**
   - Ensure `.env` files are properly configured
   - Restart development servers after changing environment variables

2. **RAG Queries Timeout**
   - Check OpenAI API key validity
   - Verify Qdrant connection and credentials

3. **Authentication Errors**
   - Confirm Better-Auth configuration
   - Check database connection for user profiles

### Getting Help

- Check the full documentation in the `docs/` directory
- Review the specification at `specs/001-textbook-spec/spec.md`
- Examine the implementation plan at `specs/001-textbook-spec/plan.md`