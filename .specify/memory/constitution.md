<!--
Sync Impact Report:
- Version change: N/A → 1.0.0 (initial creation)
- Added sections: All sections as per requirements
- Templates requiring updates: N/A (new file)
- Follow-up TODOs: None
-->

# Physical AI & Humanoid Robotics Constitution

## Core Principles

### I. Educational Excellence
All content must prioritize clear, comprehensive education in Physical AI and Humanoid Robotics; Every chapter, lesson, and example must serve pedagogical goals; Content must be technically accurate, accessible to target audience, and practically applicable.

### II. Docusaurus-Powered Publishing
All textbook content must be structured for Docusaurus publishing; Documentation follows Docusaurus conventions and best practices; Site generation, navigation, and search capabilities are core requirements; All content must render properly across different devices and browsers.

### III. RAG Integration-First (NON-NEGOTIABLE)
Every content piece must be designed for RAG retrieval; Textbook content serves as the primary knowledge base for the chatbot; RAG system uses OpenAI Agents/ChatKit SDK, FastAPI, Neon Postgres, Qdrant Cloud; Chatbot answers must be grounded in textbook content only, with no hallucinations.

### IV. Multi-Modal Learning Support
Content must support diverse learning modalities including text, code examples, simulations, and interactive elements; ROS packages, Gazebo/Unity simulations, and NVIDIA Isaac examples must be integrated throughout; Vision-Language-Action and Conversational Robotics concepts must be hands-on and practical; Capstone projects must integrate all learned concepts.

### V. Personalization & Accessibility
All content must support user personalization features; Urdu translation must be accurate and preserve technical meaning; User profiles and preferences stored securely in Neon Postgres; Authentication via Better-Auth with proper security practices; Accessibility standards must be met for all users.

### VI. Deterministic & Reproducible Content Generation
All content generation must be deterministic and reproducible; No random or non-reproducible elements allowed; Spec-Kit Plus templates must generate consistent, predictable output; Content versioning and change tracking must be precise and reliable.

## Project Scope

### Textbook Chapters Outline:
- Chapter 1: Introduction to Physical AI and Humanoid Robotics
- Chapter 2: Fundamentals of Robot Operating System (ROS 2)
- Chapter 3: Simulation Environments (Gazebo & Unity)
- Chapter 4: NVIDIA Isaac Platform and GPU-Accelerated Robotics
- Chapter 5: Vision-Language-Action Robotics
- Chapter 6: Conversational Robotics and Human-Robot Interaction
- Chapter 7: Hardware Design for Humanoid Robots
- Chapter 8: Control Systems and Motion Planning
- Chapter 9: AI and Machine Learning for Robotics
- Chapter 10: Capstone Humanoid Robot Project

### Module Specifications:
- ROS 2: Core concepts, nodes, topics, services, actions, launch files, package structure
- Gazebo & Unity: Physics simulation, model creation, environment setup, sensor integration
- NVIDIA Isaac: GPU-accelerated perception, Isaac ROS, navigation, manipulation
- Vision-Language-Action Robotics: Multi-modal AI, embodied intelligence, task planning
- Conversational Robotics: Natural language processing, dialogue systems, social robotics
- Capstone: Complete humanoid robot design, implementation, and testing

### RAG Chatbot Features:
- User-selected text-based question answering
- Context-aware responses from textbook content
- Citation of source material
- Personalized learning path recommendations
- Urdu language support for queries and responses

### User Interface Features:
- Better-Auth for secure signup/signin
- Personalization button for customized learning experience
- Urdu translation button for multilingual support
- User profile management and progress tracking

## Personas

### Student
- Learns Physical AI and Humanoid Robotics concepts
- Interacts with textbook content, examples, and simulations
- Uses RAG chatbot for Q&A and clarification
- Benefits from personalization and Urdu translation features

### Instructor
- Teaches Physical AI and Humanoid Robotics courses
- Customizes content for specific course needs
- Tracks student progress and understanding
- Uses advanced features for curriculum design

### Author
- Creates and maintains textbook content
- Develops code examples and simulation notebooks
- Ensures technical accuracy and pedagogical effectiveness
- Integrates new modules and updates existing content

### RAG Agent
- Processes user queries against textbook content
- Retrieves relevant information from embeddings
- Generates accurate, context-aware responses
- Maintains response quality and prevents hallucinations

### Subagents (Claude Code Subagents)
- Assist in content generation and maintenance
- Help implement code examples and simulations
- Support development of textbook modules
- Aid in RAG dataset creation and optimization

### Personalization Engine
- Analyzes user preferences and learning patterns
- Adapts content presentation and recommendations
- Maintains user profiles in Neon Postgres
- Customizes learning paths based on user goals

### Translation Engine (Urdu)
- Translates content from English to Urdu
- Preserves technical accuracy and meaning
- Maintains consistency across translated content
- Supports Urdu language queries in RAG system

## Core Objects

### Chapter
- Contains lessons, code examples, and exercises
- Follows Docusaurus structure and navigation
- Includes learning objectives and assessments
- Supports multimedia content integration

### Lesson
- Single learning unit with specific objectives
- Combines theory, examples, and practical exercises
- Links to related content and prerequisites
- Supports different learning modalities

### Code Example
- Standalone, executable code snippets
- Accompanied by explanations and context
- Tested and verified for accuracy
- Integrated with ROS, Gazebo, Unity, or Isaac

### Simulation Notebook
- Interactive Jupyter notebooks for simulations
- Step-by-step guided exploration
- Integration with Gazebo, Unity, or Isaac
- Hands-on learning with immediate feedback

### ROS Package Example
- Complete, functional ROS 2 packages
- Demonstrates specific concepts or techniques
- Includes launch files, configuration, and documentation
- Ready for execution in simulation or hardware

### VLA Workflow
- Vision-Language-Action integrated processes
- Demonstrates multimodal AI capabilities
- Includes perception, reasoning, and action components
- Shows real-world robotics applications

### Hardware Profile
- Specifications for humanoid robot hardware
- Component lists and integration requirements
- Performance characteristics and constraints
- Assembly and configuration instructions

### Cloud vs On-prem Lab Setup
- Documentation for both deployment options
- Resource requirements and configuration
- Performance considerations and trade-offs
- Cost analysis and scalability options

### RAG Dataset Item
- Individual content chunks for retrieval
- Properly formatted for embedding generation
- Maintains semantic coherence and context
- Links to source textbook location

### User Profile Object
- Stores user preferences and settings
- Tracks learning progress and achievements
- Maintains personalization settings
- Secured in Neon Postgres database

## Rules & Constraints

### Docusaurus Structure Rules:
- All content follows Docusaurus documentation standards
- Proper Markdown formatting with frontmatter metadata
- Navigation structure matches textbook outline
- Search indexing enabled for all content

### Repository Usage Constraints:
- No external repository usage except what Spec-Kit Plus generates
- All content must be self-contained within the project
- Dependencies managed through proper package management
- Third-party integrations documented and justified

### Content Generation Requirements:
- All content generated must be deterministic and reproducible
- Templates must produce consistent output across runs
- Random elements must be seeded for reproducibility
- Version control tracks all content changes

### RAG System Constraints:
- Only content of the textbook is allowed in embeddings for RAG
- RAG answers must only use retrieved context from textbook
- No external knowledge sources allowed in responses
- Citations must reference specific textbook sections

### Personalization Rules:
- Personalization only modifies rendering, not source content
- User preferences stored separately from core content
- Default experience remains consistent for all users
- Personalization features do not affect content accuracy

### Urdu Translation Requirements:
- Urdu translation must preserve technical accuracy
- Technical terms must be consistently translated
- Cultural appropriateness for Urdu-speaking audience
- Quality assurance for translation accuracy

## Success Criteria

### Deployment Requirements:
- Textbook deployed on GitHub Pages with proper domain
- All content accessible and properly formatted
- Search functionality working across entire textbook
- Mobile-responsive design implemented

### RAG Chatbot Requirements:
- RAG chatbot fully functional with textbook content
- Query response time under 3 seconds for typical questions
- Accuracy rate above 95% for textbook-based questions
- Proper citation of source material in responses

### Authentication Requirements:
- Better-Auth signup/signin works reliably
- User registration and login process completed
- Password reset and account management available
- Session management and security implemented

### Database Requirements:
- User profile stored in Neon Postgres with proper schema
- User preferences and personalization data persisted
- Profile data accessible and manageable
- Database connections secure and efficient

### Storage Requirements:
- Qdrant stores embeddings with proper indexing
- Content chunks properly vectorized and stored
- Retrieval performance meets response time requirements
- Embedding updates triggered on content changes

### Feature Requirements:
- Personalization button functional with user preferences
- Urdu translation button provides accurate translations
- All interactive elements work as expected
- User experience consistent across all features

## Governance

All project activities must comply with this constitution; Amendments require formal documentation and approval process; Quality gates must be passed before content publication; Development follows Spec-Kit Plus templates and workflows; All PRs/reviews must verify constitutional compliance; Complexity must be justified by clear pedagogical or technical benefits; Use this constitution as the primary guidance for all development decisions.

**Version**: 1.0.0 | **Ratified**: 2025-12-06 | **Last Amended**: 2025-12-06