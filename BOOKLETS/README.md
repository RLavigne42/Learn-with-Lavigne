# BOOKLETS Curriculum Guide

This directory organizes the learning path into four categories, each with its own `plan.md`.
The progression moves from non-technical intuition to advanced systems, architecture, and reliability engineering.

## Table of Contents

- [PRIMER](#primer)
- [BEGINNER](#beginner)
- [INTERMEDIATE](#intermediate)
- [ADVANCED](#advanced)
- [Suggested Learning Path](#suggested-learning-path)

---

## PRIMER

**File:** `BOOKLETS/PRIMER/plan.md`

### Category Synopsis
PRIMER is the conceptual on-ramp for complete newcomers. It focuses on intuition first: what AI is, how LLMs generate text, where prompting helps, and where risks appear. The content is analogy-heavy and avoids unnecessary complexity.

### Booklets in this Category
1. **What AI Really Is: An Intuitive Guide to LLMs**  
   Introduces “AI as prediction” and explains strengths/weaknesses in plain language.
2. **Understanding the Building Blocks: Language, Tokens, and Data**  
   Breaks down core parts of language AI and why data structure matters.
3. **How LLMs Get Smart: A Gentle Intro to Model Training**  
   Covers the feedback-practice loop and common under/over-learning behaviors.
4. **Thinking With Machines: How LLMs Generate Answers**  
   Explains next-token generation, prompt priming, creativity settings, and memory limits.
5. **Intro to Prompting: Talking to AI Effectively**  
   Gives practical prompt recipes with constraints, examples, and iteration habits.
6. **Intro to RAG: Helping AI Learn From Your Information**  
   Uses open-book-test intuition for document-grounded answers.
7. **Beginner Agents: How AI Can Take Actions for You**  
   Distinguishes chat-only AI from tool-using action systems.
8. **The Ecosystem: Intro to AI Tools & Workflows**  
   Explains app/API/model roles with a service-system metaphor.
9. **Beginner AI Evaluation: How to Know If AI Is Working**  
   Teaches practical quality checks and basic fact-verification routines.
10. **Safety, Ethics & Responsible AI for Beginners**  
    Covers bias, privacy, and responsible use as core user responsibilities.

---

## BEGINNER

**File:** `BOOKLETS/BEGINNER/plan.md`

### Category Synopsis
BEGINNER transitions from intuition to structured technical literacy. It introduces how model internals are organized, how specialization works, how to reason with prompts, and how real AI systems are evaluated, served, and secured.

### Booklets in this Category
1. **What is an AI “Brain”?: An Intuitive Guide to Models**  
   Layered architecture, sequence order handling, memory, and generation foundations.
2. **How to “Specialize” an AI: A Gentle Intro to Fine-Tuning**  
   Adaptation pathways from broad capability to domain-specific behavior.
3. **How to “Reason” With an AI: A Gentle Intro to Prompting**  
   Stepwise prompting methods, decomposition, format control, and self-correction.
4. **The “Stuff” That “Runs” AI: A Gentle Intro to the Ecosystem**  
   Runtime stack concepts and orchestration roles in practical systems.
5. **How AI “Remembers” Your Stuff: A Gentle Intro to RAG**  
   Retrieval workflows, chunking/indexing intuition, and grounding patterns.
6. **How AI “Sees” the World: Vision & Multimodality**  
   Text-image-audio understanding and generation basics.
7. **Beginner Agents: How AI Can Take Actions for You**  
   Agent loops, team patterns, memory/state, and human approval gates.
8. **Is the AI “Working”?: Evaluation & Testing**  
   Quality grading, tracing, drift awareness, and prompt/model version discipline.
9. **How AI “Runs” in the Real World: Serving**  
   Inference performance fundamentals: cache, batching, quantization, and edge trade-offs.
10. **How to “Trust” an AI: Safety**  
    Attack surfaces, defensive architecture, red-teaming, and privacy safeguards.

---

## INTERMEDIATE

**File:** `BOOKLETS/INTERMEDIATE/plan.md`

### Category Synopsis
INTERMEDIATE targets practitioners building robust AI applications. It deepens architecture mechanics, adaptation pipelines, programmatic prompting, ecosystem tooling, retrieval systems, orchestration, observability, and production deployment.

### Booklets in this Category
1. **LLM Fundamentals & The Transformer Architecture**  
   Full-stack transformer internals, scaling laws, context constraints, and inference mechanics.
2. **Advanced Adaptation — Fine-Tuning, PEFT, and Alignment**  
   Practical adaptation choices from full tuning to LoRA-family and preference optimization.
3. **Flow Engineering & Programmatic Prompting**  
   Prompt logic as software: modular flows, optimization, validation, and reusable templates.
4. **The Python AI Ecosystem**  
   Core Python stack from model APIs to distributed training, testing, and observability.
5. **Data Engineering & SQL for RAG**  
   Ingestion pipelines, schema strategy, SQL+embedding integration, and governance.
6. **Vector Databases & Advanced Retrieval (GraphRAG)**  
   ANN indexes, hybrid retrieval, re-ranking, graph retrieval, and secured access filtering.
7. **Agentic Patterns & Orchestration**  
   Deterministic stateful orchestration, tool pipelines, memory design, and failure handling.
8. **LLMOps: Evaluation, Tracing & Observability**  
   Metrics, eval frameworks, prompt regression testing, drift monitoring, and auditability.
9. **Production Serving & Optimization**  
   Throughput/latency optimization, quantization, parallelism, and cloud-native operations.
10. **Security, Guardrails & Future Trends**  
    Prompt-safety architecture, adversarial testing, privacy controls, and regulatory constraints.

---

## ADVANCED

**File:** `BOOKLETS/ADVANCED/plan.md`

### Category Synopsis
ADVANCED is for frontier-level builders and researchers. It spans post-transformer architectures, model surgery, formal/neuro-symbolic reasoning, low-level systems optimization, enterprise retrieval fusion, vector internals, autonomous multi-agent coordination, reliability engineering, ultra-performance inference, and adversarial AI security.

### Booklets in this Category
1. **Deep Architecture: Beyond Transformers**  
   Attention alternatives, sparsity paradigms, hybrid computation, and frontier sequence modeling.
2. **Advanced Adaptation & Model Surgery**  
   Precision interventions in weight/activation space and next-generation alignment optimization.
3. **Reasoning Systems: Advanced Prompting & Neuro-Symbolic Methods**  
   Verifiable reasoning loops, formal solver integration, search strategies, and compiler-style prompting.
4. **Advanced Python AI Engineering**  
   Kernel-level acceleration, C++ bridges, zero-copy pipelines, observability, and compiler pathways.
5. **Enterprise Knowledge Architecture & Retrieval Fusion**  
   Multi-retriever fusion, temporal/uncertainty-aware retrieval, governance, and adversarial robustness.
6. **Vector Database Internals & Search Theory**  
   Mathematical ANN theory, quantization systems, dynamic index repair, and high-churn ingestion.
7. **Autonomous Agents: High-Complexity Multi-Agent Systems**  
   Decentralized coordination, policy-governed orchestration, and resilient high-horizon autonomy.
8. **Advanced LLMOps & AI Reliability Engineering**  
   Probabilistic reliability metrics, anomaly pipelines, canaries, semantic diffs, and compliance reporting.
9. **Frontier Inference & Ultra-Performance Serving**  
   Hardware-software co-design for extreme throughput, long context, and distributed fault tolerance.
10. **Advanced AI Security & Adversarial Combat**  
    Offensive/defensive AI security, automated red teaming, side channels, and zero-trust isolation.

---

## Suggested Learning Path

1. **PRIMER** — build mental models and practical safety habits.
2. **BEGINNER** — gain foundational technical literacy and system intuition.
3. **INTERMEDIATE** — build production-ready workflows and engineering discipline.
4. **ADVANCED** — specialize in frontier architecture, optimization, and reliability/security at scale.
