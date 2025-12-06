# Data Model: Physical AI & Humanoid Robotics Textbook

**Feature**: 001-textbook-spec
**Date**: 2025-12-06
**Status**: Complete

## Entity: Student Profile

**Description**: Represents a user account with preferences, progress tracking, and personalization settings

**Fields**:
- `id`: UUID (Primary Key)
- `email`: String (Unique, Required)
- `name`: String (Required)
- `password_hash`: String (Required, Encrypted)
- `created_at`: DateTime (Required)
- `updated_at`: DateTime (Required)
- `preferred_language`: String (Default: "en", Enum: ["en", "ur"])
- `learning_preferences`: JSON (Customizable settings)
- `current_module`: Integer (Foreign Key to Module)
- `progress_percentage`: Float (0-100)
- `personalization_settings`: JSON (UI preferences, learning path)
- `is_active`: Boolean (Default: true)

**Validation Rules**:
- Email must be valid format
- Password must meet security requirements
- Preferred language must be supported
- Progress percentage between 0-100

**Relationships**:
- One-to-Many: Student Progress records
- One-to-Many: User interactions with RAG
- One-to-Many: Completed exercises

## Entity: Textbook Chapter

**Description**: Contains educational content organized by topic with learning objectives and exercises

**Fields**:
- `id`: UUID (Primary Key)
- `title`: String (Required)
- `slug`: String (Unique, Required, URL-friendly)
- `content`: Text (Required, Markdown format)
- `module_id`: UUID (Foreign Key to Module)
- `chapter_number`: Integer (Required, for ordering)
- `learning_objectives`: JSON (Array of learning objectives)
- `prerequisites`: Array of UUIDs (Other chapters required)
- `estimated_reading_time`: Integer (Minutes)
- `word_count`: Integer (For analytics)
- `difficulty_level`: String (Enum: ["beginner", "intermediate", "advanced"])
- `created_at`: DateTime (Required)
- `updated_at`: DateTime (Required)
- `is_published`: Boolean (Default: false)

**Validation Rules**:
- Title and slug must be unique within module
- Chapter number must be unique within module
- Content must be valid Markdown
- Difficulty level must be one of allowed values

**Relationships**:
- Many-to-One: Module
- One-to-Many: Exercises
- One-to-Many: Chapter interactions
- Many-to-Many: Related chapters (cross-references)

## Entity: Module

**Description**: Organized collection of chapters and exercises that form a cohesive learning unit over the 13-week course

**Fields**:
- `id`: UUID (Primary Key)
- `title`: String (Required)
- `slug`: String (Unique, Required, URL-friendly)
- `description`: Text (Required)
- `week_number`: Integer (Required, 1-13)
- `learning_goals`: JSON (Array of high-level goals)
- `prerequisites`: Array of UUIDs (Other modules required)
- `estimated_duration`: Integer (Hours)
- `is_active`: Boolean (Default: true)
- `created_at`: DateTime (Required)
- `updated_at`: DateTime (Required)

**Validation Rules**:
- Title and slug must be unique
- Week number between 1-13
- Estimated duration must be positive

**Relationships**:
- One-to-Many: Chapters
- One-to-Many: Exercises
- One-to-Many: Module progress records
- Many-to-Many: Prerequisite modules

## Entity: RAG Query

**Description**: Represents a user's question with selected text context for the AI-powered Q&A system

**Fields**:
- `id`: UUID (Primary Key)
- `student_id`: UUID (Foreign Key to Student Profile)
- `query_text`: Text (Required)
- `selected_text`: Text (Required, context from textbook)
- `chapter_id`: UUID (Foreign Key to Textbook Chapter)
- `retrieved_context`: JSON (Context retrieved from vector store)
- `ai_response`: Text (Required, response from AI)
- `confidence_score`: Float (0-1, AI confidence)
- `query_timestamp`: DateTime (Required)
- `feedback_rating`: Integer (1-5, optional)
- `feedback_comment`: Text (Optional)
- `is_resolved`: Boolean (Default: false)

**Validation Rules**:
- Query text must not be empty
- Confidence score between 0-1
- Feedback rating between 1-5 if provided

**Relationships**:
- Many-to-One: Student Profile
- Many-to-One: Textbook Chapter
- One-to-Many: Query analytics

## Entity: Simulation Environment

**Description**: Represents an interactive learning space (Gazebo, Unity, Isaac Sim) for hands-on experience

**Fields**:
- `id`: UUID (Primary Key)
- `name`: String (Required)
- `type`: String (Enum: ["gazebo", "unity", "isaac", "ros"])
- `description`: Text (Required)
- `chapter_id`: UUID (Foreign Key to Textbook Chapter)
- `config_file_path`: String (Path to simulation config)
- `requirements`: JSON (System requirements)
- `estimated_completion_time`: Integer (Minutes)
- `difficulty_level`: String (Enum: ["beginner", "intermediate", "advanced"])
- `is_active`: Boolean (Default: true)
- `created_at`: DateTime (Required)
- `updated_at`: DateTime (Required)

**Validation Rules**:
- Name must be unique within chapter
- Type must be one of allowed values
- Difficulty level must be one of allowed values

**Relationships**:
- Many-to-One: Textbook Chapter
- One-to-Many: Simulation attempts
- One-to-Many: Simulation feedback

## Entity: Exercise

**Description**: Interactive problems and activities associated with chapters and modules

**Fields**:
- `id`: UUID (Primary Key)
- `title`: String (Required)
- `description`: Text (Required)
- `chapter_id`: UUID (Foreign Key to Textbook Chapter)
- `module_id`: UUID (Foreign Key to Module)
- `exercise_type`: String (Enum: ["multiple_choice", "coding", "simulation", "essay"])
- `difficulty_level`: String (Enum: ["beginner", "intermediate", "advanced"])
- `estimated_completion_time`: Integer (Minutes)
- `content`: Text (Exercise content in Markdown)
- `solution`: Text (Hidden solution)
- `scoring_criteria`: JSON (How to grade the exercise)
- `is_active`: Boolean (Default: true)
- `created_at`: DateTime (Required)
- `updated_at`: DateTime (Required)

**Validation Rules**:
- Exercise type must be one of allowed values
- Difficulty level must be one of allowed values
- Solution must exist for auto-gradable exercises

**Relationships**:
- Many-to-One: Textbook Chapter
- Many-to-One: Module
- One-to-Many: Exercise submissions
- One-to-Many: Exercise analytics

## Entity: Embedding Chunk

**Description**: Represents a segment of textbook content converted to vector format for RAG retrieval

**Fields**:
- `id`: UUID (Primary Key)
- `content`: Text (Required, the actual text chunk)
- `chapter_id`: UUID (Foreign Key to Textbook Chapter)
- `chunk_index`: Integer (Position within chapter)
- `vector_embedding`: JSON (Vector representation)
- `token_count`: Integer (Number of tokens in chunk)
- `semantic_boundary`: Boolean (True if natural boundary)
- `created_at`: DateTime (Required)
- `updated_at`: DateTime (Required)

**Validation Rules**:
- Content must not be empty
- Token count must be positive
- Vector embedding must be valid format

**Relationships**:
- Many-to-One: Textbook Chapter
- One-to-Many: RAG query results

## Entity: Student Progress

**Description**: Tracks student progress through chapters, modules, and exercises

**Fields**:
- `id`: UUID (Primary Key)
- `student_id`: UUID (Foreign Key to Student Profile)
- `chapter_id`: UUID (Foreign Key to Textbook Chapter)
- `module_id`: UUID (Foreign Key to Module)
- `exercise_id`: UUID (Foreign Key to Exercise, optional)
- `progress_percentage`: Float (0-100)
- `time_spent_seconds`: Integer (Time spent on content)
- `completed_at`: DateTime (When completed, optional)
- `attempts_count`: Integer (Number of attempts)
- `score`: Float (0-100, for graded content)
- `status`: String (Enum: ["not_started", "in_progress", "completed", "passed", "failed"])
- `last_accessed_at`: DateTime (Required)
- `created_at`: DateTime (Required)
- `updated_at`: DateTime (Required)

**Validation Rules**:
- Progress percentage between 0-100
- Score between 0-100 if provided
- Status must be one of allowed values

**Relationships**:
- Many-to-One: Student Profile
- Many-to-One: Textbook Chapter
- Many-to-One: Module
- Many-to-One: Exercise (if applicable)

## Entity: Translation Content

**Description**: Represents Urdu translations of textbook content with preserved technical meaning

**Fields**:
- `id`: UUID (Primary Key)
- `original_content_id`: UUID (Foreign Key to original content - Chapter, Exercise, etc.)
- `content_type`: String (Enum: ["chapter", "exercise", "module", "interface"])
- `original_text`: Text (Required, original English content)
- `translated_text`: Text (Required, Urdu translation)
- `translation_accuracy_score`: Float (0-1, quality score)
- `reviewed_by`: UUID (Foreign Key to reviewer profile)
- `reviewed_at`: DateTime (When reviewed, optional)
- `is_approved`: Boolean (Default: false)
- `created_at`: DateTime (Required)
- `updated_at`: DateTime (Required)

**Validation Rules**:
- Original and translated text must not be empty
- Accuracy score between 0-1
- Content type must be one of allowed values

**Relationships**:
- One-to-One: Original content (Chapter, Exercise, etc.)