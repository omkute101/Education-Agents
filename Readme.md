# Base Agent – Multi-Agent Personalized Education System (GDG Project)

## 1. Overview

This project implements a **modular, multi-agent AI system for personalized education** using **Google ADK**, **Python**, and **machine-learning models**.

Instead of building a single generic chatbot, the system is designed around **specialized agents**, each responsible for a specific decision or reasoning task.  
The focus of this project is **architecture, personalization, and intelligent orchestration**, not just answering questions.

---

## 2. Problem Statement

Most existing educational chatbots suffer from the following issues:
- They provide generic answers to all users
- They ignore user emotion and learning state
- They mix reasoning, execution, and UI logic
- They are hard to personalize or scale

This project solves these problems by:
- Using **multiple specialized agents**
- Separating **decision-making from execution**
- Designing for **personalization by default**
- Keeping the system **backend-ready and extensible**

---

## 3. Core Design Principles

### 3.1 Multi-Agent Architecture
Each agent has **one clear responsibility**.  
No agent tries to do everything.

### 3.2 Decision ≠ Execution
Agents only decide **what should happen**.  
Execution (UI rendering, backend calls, notifications, image generation) is handled externally.

### 3.3 Loose Coupling
Agents:
- do NOT call each other directly
- do NOT share internal state
- communicate only via **structured context and JSON outputs**

### 3.4 Personalization First
The system adapts to:
- user emotion
- learning state
- progress trends
- (future) user preferences and memory

---

## 4. High-Level System Flow

Each step is handled by a **different agent**, making the system modular and explainable.

---

## 5. Agents Implemented

### 5.1 Emotion / Sentiment Agent
**Purpose:** Detect how the user is feeling while learning.

**How it works:**
- Uses a Hugging Face emotion classification model
- Detects emotions from user text
- Maps raw emotions into learning-centric states:
  - frustrated
  - confused
  - calm
  - motivated

**Why this matters:**  
Learning effectiveness depends heavily on emotional state.  
This agent enables adaptive responses instead of generic replies.

---

### 5.2 Motivation & Feedback Agent (Google ADK)
**Purpose:** Provide human-like encouragement and feedback.

**Inputs:**
- learning_state
- optional recent context

**Outputs (JSON):**
- tone
- short motivational message

**Constraints:**
- No teaching
- No long plans
- 1–2 sentences only

**Why Google ADK:**  
Tone, empathy, and encouragement require language reasoning.

---

### 5.3 Analytics Insight Agent (Google ADK)
**Purpose:** Explain learning progress in natural language.

**How it works:**
- Receives structured progress data (attempts, averages, trends)
- Highlights strengths and weak areas
- Gives high-level improvement guidance

**Design choice:**
- Python → numeric calculations
- ADK → explanation and insights

---

### 5.4 Resource Decision Agent (Google ADK)
**Purpose:** Decide *what kind of learning support is needed*.

**Decisions include:**
- Is a resource needed?
- Explanation vs visual vs notes
- Difficulty level (beginner / intermediate / advanced)

**Important:**  
This agent **does not generate or fetch content**.  
It only decides *what should be done next*.

---

### 5.5 Image Generation Decision Agent (Google ADK)
**Purpose:** Decide when visuals improve learning.

**What it does:**
- Determines if an image is useful
- Chooses image type (diagram, flowchart, illustration)
- Generates a structured image prompt

**What it does NOT do:**
- No image generation
- No API calls
- No file handling

Actual image generation will be handled externally.

---

### 5.6 Reminder Decision Agent (Google ADK)
**Purpose:** Decide if and when learning reminders are required.

**Inputs:**
- user progress
- learning state
- inactivity duration

**Outputs (JSON):**
- send_reminder (true/false)
- reminder_type
- timing
- reason

**Note:**  
Notification delivery is planned via **MCP-based execution** (email / push) in future.

---

## 6. Base Agent (Demo Host)

The main project host agent was not available during development.  
Therefore, a **base agent** is implemented to:

- demonstrate orchestration
- show how agents are interconnected
- enable local testing and ADK Web demo

The base agent:
- does NOT replace the final production host
- does NOT hardcode workflows
- exists only to demonstrate architecture and integration

---

## 7. Project Structure

Each folder is a Python package with its own `__init__.py`.

---

## 8. Memory & Personalization

A memory adapter layer is included to:
- read user profile information
- respect memory on/off preferences
- prepare for backend database integration

Agents themselves remain **stateless** to ensure scalability.

---

## 9. Environment Configuration

Create a `.env` file (never commit this file):

```env
GOOGLE_API_KEY=your_gemini_api_key
GOOGLE_GENAI_USE_VERTEX_AI=false




