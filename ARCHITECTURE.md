# System Architecture & Responsible AI Guardrails

## End-to-End Workflow

~~~mermaid
flowchart LR
    A[Raw Incident Telemetry] --> B[Agent 1: Classifier & Confidence Scorer]
    B -->|Confidence < 0.80| C[Human-in-the-Loop Queue]
    B -->|Confidence >= 0.80| D[Agent 2: Ecosystem & Dependency Risk]
    D --> E[Agent 3: Executive Brief Synthesizer]
    E --> F[VP/SVP Weekly Decision Brief]
~~~

## Architectural Trade-Offs (Tool-Agnostic Design)
- **Decoupled Prompts (`agents/*.md`):** Separating agent instructions from orchestration code allows non-engineering domain experts to audit and refine business rules without touching Python.
- **Confidence Gating:** Enforcing a strict `0.80` confidence threshold prevents low-certainty classifications or silent hallucinations from skewing executive reporting.
- **Model Portability:** The orchestration layer communicates via standard JSON payloads, allowing the underlying LLM runtime (local Ollama or enterprise API) to be swapped without rewriting agent rules.
