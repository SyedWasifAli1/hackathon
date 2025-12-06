---
id: 1
title: Generate Physical AI Constitution
stage: constitution
date: 2025-12-06
surface: agent
model: Claude Sonnet 4.5
feature: none
branch: master
user: user
command: /sp.constitution
labels: [constitution,specification,physical-ai,robotics]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - .specify/memory/constitution.md
tests:
 - none
---

## Prompt

```text
You are the Specification Constitution Generator for Spec-Kit Plus.
Create a complete `constitution.md` for a full textbook project titled:

**"Physical AI & Humanoid Robotics"**

The constitution must define the *entire architecture* of the project.

Include the following sections:

# 1. Mission & Vision
Describe the purpose of this textbook:
- Teach Physical AI
- Teach Humanoid Robotics
- Use Docusaurus for publishing
- Integrate RAG Chatbot using OpenAI Agents/ChatKit SDK, FastAPI, Neon Postgres, Qdrant Cloud
- Support user-selected text-based QA
- Support personalization
- Support Urdu translation

# 2. Project Scope
Define clearly:
- Textbook chapters (full outline)
- Each module from course outline:
  - ROS 2
  - Gazebo & Unity
  - NVIDIA Isaac
  - Vision-Language-Action Robotics
  - Conversational Robotics
  - Capstone Humanoid Robot project
- RAG chatbot features
- Better-Auth signup/signin
- Personalization button
- Urdu translation button

# 3. Personas
Include roles:
- Student
- Instructor
- Author
- RAG Agent
- Subagents (Claude Code Subagents)
- Personalization Engine
- Translation Engine (Urdu)

# 4. Core Objects
Define reusable objects:
- Chapter
- Lesson
- Code Example
- Simulation Notebook
- ROS Package Example
- VLA Workflow
- Hardware Profile
- Cloud vs On-prem lab setup
- RAG Dataset Item
- User Profile Object

# 5. Rules & Constraints
Specify:
- Docusaurus structure rules
- No repository usage except what Spec-Kit Plus generates
- All content generated must be deterministic and reproducible
- Only content of the textbook is allowed in embeddings for RAG
- RAG answers must only use retrieved context
- Personalization only modifies rendering, not source
- Urdu translation must preserve technical accuracy

# 6. Success Criteria
Define the conditions for a successful project:
- Textbook deployed on GitHub Pages
- RAG chatbot fully functional
- Better-Auth signup/signin works
- User profile stored in Neon Postgres
- Qdrant stores embeddings
- Personalization & Urdu translation buttons functional
```

## Response snapshot

Created a complete constitution.md file for the "Physical AI & Humanoid Robotics" textbook project with all required sections including Core Principles, Project Scope, Personas, Core Objects, Rules & Constraints, Success Criteria, and Governance. The constitution defines the entire architecture of the project with specific details for each required section.

## Outcome

- ✅ Impact: Created complete project constitution at .specify/memory/constitution.md with all required sections
- 🧪 Tests: none
- 📁 Files: 1 file created (.specify/memory/constitution.md)
- 🔁 Next prompts: Continue with spec, plan, and task generation for the textbook
- 🧠 Reflection: Constitution successfully created with all required elements including textbook chapters, module specifications, personas, core objects, and success criteria.

## Evaluation notes (flywheel)

- Failure modes observed: none
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): N/A