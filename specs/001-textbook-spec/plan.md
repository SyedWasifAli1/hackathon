# Implementation Plan: Physical AI & Humanoid Robotics Textbook

**Branch**: `001-textbook-spec` | **Date**: 2025-12-06 | **Spec**: [specs/001-textbook-spec/spec.md](../specs/001-textbook-spec/spec.md)
**Input**: Feature specification from `/specs/[###-feature-name]/spec.md`

**Note**: This template is filled in by the `/sp.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

Development of a comprehensive Physical AI & Humanoid Robotics textbook using Docusaurus with integrated RAG chatbot, multilingual support (Urdu), personalization features, and interactive learning modules covering ROS 2, Gazebo, Unity, Isaac Sim, VLA pipelines, and conversational robotics. The system will include authentication via Better-Auth and be deployed to GitHub Pages.

## Technical Context

**Language/Version**: JavaScript/TypeScript, Python 3.11 for backend services
**Primary Dependencies**: Docusaurus, FastAPI, OpenAI SDK, Better-Auth, Qdrant, Neon Postgres
**Storage**: Qdrant vector store for embeddings, Neon Postgres for user profiles
**Testing**: Jest for frontend, pytest for backend
**Target Platform**: Web application (GitHub Pages/Vercel deployment)
**Project Type**: Web
**Performance Goals**: RAG responses under 3 seconds, 99% uptime, 1000 concurrent users
**Constraints**: <3 second p95 RAG response time, accessible interface, multilingual support
**Scale/Scope**: 1000+ students, 10 chapters with modules, 100+ interactive examples

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- Educational Excellence: All content must prioritize clear, comprehensive education in Physical AI and Humanoid Robotics
- Docusaurus-Powered Publishing: All textbook content must be structured for Docusaurus publishing
- RAG Integration-First: Every content piece must be designed for RAG retrieval; Textbook content serves as the primary knowledge base for the chatbot
- Multi-Modal Learning Support: Content must support diverse learning modalities including text, code examples, simulations, and interactive elements
- Personalization & Accessibility: All content must support user personalization features; Urdu translation must be accurate and preserve technical meaning
- Deterministic & Reproducible Content Generation: All content generation must be deterministic and reproducible

## Project Structure

### Documentation (this feature)

```text
specs/001-textbook-spec/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (/sp.plan command)
├── data-model.md        # Phase 1 output (/sp.plan command)
├── quickstart.md        # Phase 1 output (/sp.plan command)
├── contracts/           # Phase 1 output (/sp.plan command)
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)

```text
docs/
├── chapters/
├── modules/
└── tutorials/

rag-server/
├── src/
│   ├── api/
│   ├── models/
│   ├── services/
│   └── main.py
├── requirements.txt
└── Dockerfile

auth/
├── src/
│   ├── auth/
│   └── models/
├── requirements.txt

components/
├── chatbot/
├── personalization/
└── translation/

skills/
├── ros/
├── simulation/
└── rag/

subagents/
├── content-writer/
├── ros-generator/
└── translation/

data/embeddings/
├── textbook-chunks/
└── metadata/

i18n/ur/
├── chapters/
└── components/

scripts/
├── build-embeddings.py
├── deploy.sh
└── generate-content.py

frontend/
├── src/
│   ├── pages/
│   ├── components/
│   └── hooks/
└── docusaurus.config.js

backend/
├── src/
│   ├── rag/
│   ├── auth/
│   └── personalization/
└── requirements.txt
```

**Structure Decision**: Web application structure with frontend (Docusaurus) and backend (FastAPI) separation. The frontend handles content presentation and user interface, while the backend manages RAG, authentication, and personalization services.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| Multi-repo structure | Need to separate frontend and backend for scalability | Single repo would create deployment and maintenance complexity |

## Phase 0: Research & Analysis

### Research Tasks

1. **Docusaurus Implementation Research**
   - **Description**: Research best practices for implementing a comprehensive textbook with Docusaurus
   - **Files affected**: research.md
   - **Commands to run**: N/A
   - **Expected output**: Best practices summary for textbook structure
   - **Acceptance criteria**: Research document with Docusaurus recommendations

2. **RAG Architecture Research**
   - **Description**: Research optimal RAG implementation for educational content
   - **Files affected**: research.md
   - **Commands to run**: N/A
   - **Expected output**: RAG architecture recommendations
   - **Acceptance criteria**: Research document with RAG implementation strategies

3. **Better-Auth Integration Research**
   - **Description**: Research Better-Auth implementation for textbook platform
   - **Files affected**: research.md
   - **Commands to run**: N/A
   - **Expected output**: Authentication system recommendations
   - **Acceptance criteria**: Research document with auth implementation details

4. **Urdu Translation Strategy Research**
   - **Description**: Research technical translation strategies for Urdu
   - **Files affected**: research.md
   - **Commands to run**: N/A
   - **Expected output**: Translation implementation strategy
   - **Acceptance criteria**: Research document with translation approach

## Phase 1: Docusaurus Project Creation

### Task 1.1: Initialize Docusaurus Project
- **Description**: Set up the basic Docusaurus project structure for the textbook
- **Files affected**: package.json, docusaurus.config.js, docs/
- **Commands to run**:
  ```bash
  npx create-docusaurus@latest textbook-physical-ai classic
  cd textbook-physical-ai
  ```
- **Expected output**: Basic Docusaurus project structure
- **Acceptance criteria**: Docusaurus project runs locally with default content

### Task 1.2: Configure Docusaurus for Textbook Structure
- **Description**: Configure Docusaurus with textbook-specific navigation and layout
- **Files affected**: docusaurus.config.js, src/css/custom.css, sidebars.js
- **Commands to run**: N/A
- **Expected output**: Configured navigation matching textbook chapters and modules
- **Acceptance criteria**: Textbook navigation structure implemented with proper organization

### Task 1.3: Set Up Internationalization
- **Description**: Configure Docusaurus for multilingual support including Urdu
- **Files affected**: docusaurus.config.js, i18n/
- **Commands to run**:
  ```bash
  mkdir -p i18n/ur/docusaurus-plugin-content-docs/current
  ```
- **Expected output**: I18n configuration for English and Urdu
- **Acceptance criteria**: Internationalization framework ready for Urdu content

## Phase 2: Generate All Textbook Chapters

### Task 2.1: Create Chapter Directory Structure
- **Description**: Create the directory structure for all textbook chapters
- **Files affected**: docs/chapters/, docs/modules/
- **Commands to run**:
  ```bash
  mkdir -p docs/{chapters,modules}
  ```
- **Expected output**: Properly organized chapter and module directories
- **Acceptance criteria**: All required chapter directories exist

### Task 2.2: Generate Chapter Content
- **Description**: Create content for all textbook chapters using Claude Code
- **Files affected**: docs/chapters/*.md, docs/modules/*.md
- **Commands to run**: Claude Code content generation
- **Expected output**: Complete textbook content with chapters and modules
- **Acceptance criteria**: All 10 chapters with complete content and exercises

### Task 2.3: Add Code Examples and Diagrams
- **Description**: Include ROS 2 examples, Isaac workflows, VLA pipelines with Mermaid diagrams
- **Files affected**: docs/chapters/*.md, docs/modules/*.md
- **Commands to run**: Claude Code diagram and example generation
- **Expected output**: Technical content with code examples and visual diagrams
- **Acceptance criteria**: All chapters include relevant code examples and diagrams

## Phase 3: Install & Configure RAG Backend

### Task 3.1: Set Up FastAPI Backend
- **Description**: Create FastAPI server for RAG functionality
- **Files affected**: rag-server/src/main.py, rag-server/requirements.txt
- **Commands to run**:
  ```bash
  mkdir -p rag-server/src
  touch rag-server/src/main.py
  ```
- **Expected output**: Basic FastAPI server structure
- **Acceptance criteria**: FastAPI server runs and responds to requests

### Task 3.2: Integrate OpenAI SDK
- **Description**: Add OpenAI SDK for ChatCompletions Agent integration
- **Files affected**: rag-server/requirements.txt, rag-server/src/main.py
- **Commands to run**:
  ```bash
  pip install openai
  ```
- **Expected output**: OpenAI SDK integrated into backend
- **Acceptance criteria**: OpenAI API calls work from backend

### Task 3.3: Configure Qdrant Vector Store
- **Description**: Set up Qdrant for storing textbook embeddings
- **Files affected**: rag-server/src/services/vector_store.py
- **Commands to run**:
  ```bash
  pip install qdrant-client
  ```
- **Expected output**: Qdrant client integrated and configured
- **Acceptance criteria**: Vector store operations work correctly

### Task 3.4: Implement RAG Pipeline
- **Description**: Create complete RAG pipeline from text extraction to query response
- **Files affected**: rag-server/src/services/rag_service.py, rag-server/src/api/rag.py
- **Commands to run**: N/A
- **Expected output**: Complete RAG pipeline implementation
- **Acceptance criteria**: RAG system retrieves relevant content and generates responses

## Phase 4: Build Better-Auth Login/Signup

### Task 4.1: Install Better-Auth
- **Description**: Set up Better-Auth for user authentication
- **Files affected**: auth/src/auth/index.ts, package.json
- **Commands to run**:
  ```bash
  npm install @better-auth/node
  ```
- **Expected output**: Better-Auth package installed
- **Acceptance criteria**: Better-Auth dependency available

### Task 4.2: Configure Authentication Database
- **Description**: Set up Neon Postgres schema for user profiles
- **Files affected**: auth/src/models/user.ts
- **Commands to run**:
  ```bash
  npm install @neondatabase/serverless
  ```
- **Expected output**: Database schema for user profiles
- **Acceptance criteria**: User profile storage configured

### Task 4.3: Implement Signup/Signin UI
- **Description**: Create frontend components for authentication
- **Files affected**: frontend/src/components/auth/
- **Commands to run**: N/A
- **Expected output**: Authentication UI components
- **Acceptance criteria**: Users can signup and signin successfully

## Phase 5: Build Personalization System

### Task 5.1: Design Personalization Data Model
- **Description**: Create data structures for user preferences and learning paths
- **Files affected**: backend/src/models/personalization.py
- **Commands to run**: N/A
- **Expected output**: Personalization data model
- **Acceptance criteria**: Data model supports all required personalization features

### Task 5.2: Implement Personalization API
- **Description**: Create API endpoints for personalization features
- **Files affected**: backend/src/api/personalization.py
- **Commands to run**: N/A
- **Expected output**: Personalization API endpoints
- **Acceptance criteria**: Personalization features work via API

### Task 5.3: Create Personalization UI Components
- **Description**: Implement frontend components for personalization
- **Files affected**: frontend/src/components/personalization/
- **Commands to run**: N/A
- **Expected output**: Personalization UI components
- **Acceptance criteria**: Users can customize their learning experience

## Phase 6: Add Urdu Translation Toggle

### Task 6.1: Implement Translation Engine
- **Description**: Create Urdu translation functionality for textbook content
- **Files affected**: components/translation/translation-service.js
- **Commands to run**: N/A
- **Expected output**: Translation service for Urdu content
- **Acceptance criteria**: Content can be accurately translated to Urdu

### Task 6.2: Create Translation Toggle Component
- **Description**: Add UI component for language switching
- **Files affected**: frontend/src/components/translation/
- **Commands to run**: N/A
- **Expected output**: Language toggle UI component
- **Acceptance criteria**: Users can switch between English and Urdu

### Task 6.3: Translate Content
- **Description**: Generate Urdu translations for all textbook content
- **Files affected**: i18n/ur/chapters/, i18n/ur/modules/
- **Commands to run**: Claude Code translation
- **Expected output**: Complete Urdu translations
- **Acceptance criteria**: All content available in Urdu with technical accuracy

## Phase 7: Integrate Chatbot UI into Docusaurus

### Task 7.1: Create Chatbot Component
- **Description**: Build the RAG-powered chatbot UI component
- **Files affected**: frontend/src/components/chatbot/
- **Commands to run**: N/A
- **Expected output**: Chatbot UI component
- **Acceptance criteria**: Chatbot UI integrates seamlessly with Docusaurus

### Task 7.2: Connect Chatbot to RAG Backend
- **Description**: Connect the UI to the RAG backend service
- **Files affected**: frontend/src/services/rag-api.js
- **Commands to run**: N/A
- **Expected output**: Working connection between UI and backend
- **Acceptance criteria**: Chatbot can send queries and receive responses

### Task 7.3: Implement Text Selection Feature
- **Description**: Enable users to select text and ask questions about it
- **Files affected**: frontend/src/hooks/text-selection.js
- **Commands to run**: N/A
- **Expected output**: Text selection and context passing functionality
- **Acceptance criteria**: Users can select text and ask targeted questions

## Phase 8: Deployment to GitHub Pages/Vercel

### Task 8.1: Configure GitHub Actions
- **Description**: Set up CI/CD pipeline for GitHub Pages deployment
- **Files affected**: .github/workflows/deploy.yml
- **Commands to run**: N/A
- **Expected output**: Deployment workflow configuration
- **Acceptance criteria**: Automatic deployment on push to main branch

### Task 8.2: Set Up Backend Deployment
- **Description**: Configure backend deployment to Vercel or similar platform
- **Files affected**: vercel.json, Dockerfile
- **Commands to run**: N/A
- **Expected output**: Backend deployment configuration
- **Acceptance criteria**: Backend services deploy automatically

### Task 8.3: Deploy Production System
- **Description**: Deploy the complete system to production
- **Files affected**: All deployed files
- **Commands to run**:
  ```bash
  npm run build && npm run deploy
  ```
- **Expected output**: Live production system
- **Acceptance criteria**: All features work in production environment

## Phase 9: Demo Video Preparation

### Task 9.1: Create Demo Script
- **Description**: Write script for demonstration video
- **Files affected**: docs/demo-script.md
- **Commands to run**: N/A
- **Expected output**: Complete demo script
- **Acceptance criteria**: Script covers all key features

### Task 9.2: Record Demo Video
- **Description**: Record and edit demonstration video
- **Files affected**: docs/demo.mp4
- **Commands to run**: N/A
- **Expected output**: High-quality demo video
- **Acceptance criteria**: Video demonstrates all key features effectively

## Auto-Generated Content Tasks

### Content Generation with Claude Code
1. **Chapter Writing**: Claude Code will generate textbook chapters following the 13-week course outline
2. **Example Creation**: Claude Code will create code examples for ROS 2, Isaac, and VLA concepts
3. **Diagram Generation**: Claude Code will create Mermaid diagrams for system architectures
4. **ROS Code Samples**: Claude Code will generate functional ROS 2 package examples
5. **Isaac Workflows**: Claude Code will create Isaac Sim workflow examples
6. **VLA Pipelines**: Claude Code will design Vision-Language-Action pipeline examples

## RAG Pipeline Plan

### Step 1: Extract Docs
- Extract content from Docusaurus markdown files
- Parse text while preserving structure and context
- Output: Raw text chunks with metadata

### Step 2: Chunk Text
- Split text into semantic chunks (paragraphs, sections)
- Maintain context boundaries and relationships
- Output: Processed text chunks with context markers

### Step 3: Generate Embeddings
- Convert text chunks to vector embeddings using OpenAI API
- Store embedding metadata for retrieval
- Output: Vector embeddings with source mapping

### Step 4: Push to Qdrant
- Upload embeddings to Qdrant vector store
- Index for efficient similarity search
- Output: Indexed vector database

### Step 5: Query Pipeline
- Accept user queries with selected text context
- Perform similarity search in vector store
- Generate responses using OpenAI ChatCompletions
- Output: Contextually relevant answers

## Auth Plan

### Better-Auth Implementation
- User registration and login with email/password
- Session management and security tokens
- Profile storage in Neon Postgres
- Integration with personalization features
- Secure API access for all backend services