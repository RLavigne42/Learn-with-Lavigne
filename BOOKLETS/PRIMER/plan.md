# PRIMER Plan

## BOOKLET 1 — What AI Really Is: An Intuitive Guide to LLMs
### 1. Introduction: What is 'Thinking' for a Computer?
- **url_slug:** `primer/intro-what-is-ai`
- **prompt:** Provide a deeply intuitive, high-level, and analogy-rich introduction to Large Language Models (LLMs) for a complete beginner, assuming zero technical knowledge. The primary goal is to build a conceptual 'feel' for AI, not a technical definition. This prompt must strictly avoid all jargon (e.g., 'parameters', 'training', 'architecture', 'model'). Explain:
  1. What 'smart' means for a computer (e.g., world-class parrot, predictive autocomplete).
  2. How machines 'learn' from patterns (e.g., reading all books in a library to see what words appear together).
  3. Why LLMs do not 'think' or 'feel' like humans, but act as prediction engines for text.
  4. Hallucinations via a simple metaphor (e.g., a student confidently guessing instead of saying "I don't know").
  5. Why data quality matters (e.g., if it only reads sad books, it develops a sad worldview).
  6. Core strengths (summarizing, rephrasing) vs weaknesses (no truth-understanding, weak common sense).

## BOOKLET 2 — Understanding the Building Blocks: Language, Tokens, and Data
### 1. Introduction: The 'Lego Blocks' of AI Language
- **url_slug:** `primer/blocks-tokens-data`
- **prompt:** Provide a foundational, conceptual explanation of LLM components with simple metaphors and no code/jargon. Must include:
  1. 'Lego Blocks' analogy for tokens.
  2. Data as the AI's library/collection of books.
  3. Structured vs unstructured data (organized spreadsheet vs messy notes/books).
  4. Model size without using the word 'parameters' (e.g., size of AI brain / capacity).
  5. Fine-tuning as 'special lessons' on focused subject matter.

## BOOKLET 3 — How LLMs Get Smart: A Gentle Intro to Model Training
### 1. Introduction: How an AI 'Practices' to Get Better
- **url_slug:** `primer/training-how-llms-learn`
- **prompt:** Provide a beginner-friendly conceptual overview of training using analogies and without technical optimization terms. Must include:
  1. Guess → feedback → improve loop (flashcard student analogy).
  2. Why training takes so long (massive scale of practice).
  3. Overfitting as memorizing test answers without understanding.
  4. Underfitting as not studying enough.
  5. Forgetting after new focused learning.

## BOOKLET 4 — Thinking With Machines: How LLMs Generate Answers
### 1. Introduction: How an AI Decides 'What's Next?'
- **url_slug:** `primer/generation-how-llms-think`
- **prompt:** Provide an intuitive guide to answer generation without terms like inference/autoregressive/KV cache. Must include:
  1. Super-autocomplete as next-word prediction.
  2. Prompts as starting point.
  3. Temperature as creativity slider.
  4. Context limits as short-term memory limits (without saying 'window').
  5. Why repetition loops happen.

## BOOKLET 5 — Intro to Prompting: Talking to AI Effectively
### 1. Introduction: The 'Recipe' for a Good AI Answer
- **url_slug:** `primer/prompting-basics`
- **prompt:** Provide a practical beginner guide for better prompts using simple actionable rules. Must include:
  1. Bad vs Good prompt examples.
  2. Giving the AI a role.
  3. Adding constraints (length, tone, audience).
  4. Providing output examples/templates.
  5. Iteration and rephrasing for improved results.

## BOOKLET 6 — Intro to RAG: Helping AI Learn From Your Information
### 1. Introduction: The 'Open-Book Test' for AI
- **url_slug:** `primer/rag-open-book-analogy`
- **prompt:** Provide a conceptual explanation using only plain language and avoiding technical retrieval terms. Must include:
  1. Open-book vs closed-book test analogy.
  2. Breaking long documents into smaller pieces using a simple metaphor.
  3. Searching those pieces to find relevant passages.
  4. Why this helps: private knowledge grounding + source citation.

## BOOKLET 7 — Beginner Agents: How AI Can Take Actions for You
### 1. Introduction: Giving the AI 'Hands' to Help You
- **url_slug:** `primer/agents-ai-with-hands`
- **prompt:** Provide an intuitive introduction to agents using plain language. Must include:
  1. Brain vs Hands analogy.
  2. Tool examples (search, calculator, email).
  3. Step-by-step agent task walkthrough (weather + email example).
  4. Human approval as safety latch before final actions.

## BOOKLET 8 — The Ecosystem: Intro to AI Tools & Workflows
### 1. Introduction: The 'AI Restaurant' - What Happens Behind the Scenes
- **url_slug:** `primer/ecosystem-restaurant-analogy`
- **prompt:** Explain the AI stack using the Restaurant Analogy for non-technical users. Must include:
  1. App = Menu, API = Waiter, Model = Kitchen.
  2. Cloud vs Local (power/public vs slower/private).
  3. Enterprise AI vs Personal AI using kitchen scale analogy.

## BOOKLET 9 — Beginner AI Evaluation: How to Know If AI Is Working
### 1. Introduction: How to 'Fact-Check' Your AI
- **url_slug:** `primer/evaluation-fact-checking`
- **prompt:** Provide a non-technical checklist for evaluating answer quality. Must include:
  1. Beginner QA checklist (plausibility, relevance, verification).
  2. Hallucinations explained in plain terms.
  3. A self-critique prompt users can ask AI when unsure.

## BOOKLET 10 — Safety, Ethics & Responsible AI for Beginners
### 1. Introduction: Being a 'Responsible Pilot' for AI
- **url_slug:** `primer/safety-responsible-pilot`
- **prompt:** Provide a conceptual safety/ethics guide for beginners. Must include:
  1. AI engine vs human pilot analogy.
  2. Bias through skewed reading sources.
  3. Data safety (avoid sharing sensitive/private info in public AI).
  4. Responsible use and accountability.
  5. Confidently wrong answers as top beginner safety risk and need for verification.

---

## Notes
- Source JSON fields `model` and `temperature` were intentionally omitted per request to disregard model information.
