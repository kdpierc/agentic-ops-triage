# Agentic Ops Triage & Executive Telemetry Pipeline

A tool-agnostic, multi-agent workflow demonstrating how operational incident telemetry is classified, evaluated for downstream ecosystem risk, and synthesized into weekly executive decision briefs—with built-in human-in-the-loop (HITL) confidence guardrails.

## Problem Statement
High-volume operational environments generate hundreds of recurring incident tickets every month. Manual triage slows root-cause discovery and obscures systemic risks across dependent facilities and services.

## Architecture Overview
This pipeline decouples **agent instructions & guardrails** (`agents/*.md`) from **orchestration logic** (`run_pipeline.py`), allowing domain leads to audit and refine operational rules independently of application code:

1. **Agent 1 (`01_triage_agent.md`):** Classifies raw incident records by root-cause domain and severity, assigning a confidence score and flagging low-confidence items (`< 0.80`) for human review.
2. **Agent 2 (`02_risk_agent.md`):** Evaluates classified incidents for recurring patterns, cross-service dependencies, and downstream operational exposure.
3. **Agent 3 (`03_exec_brief_agent.md`):** Synthesizes validated findings into a structured weekly executive brief with prioritized recommendations.

See [`ARCHITECTURE.md`](./ARCHITECTURE.md) for system diagrams and trade-off analysis.

## How to Run Locally (Using Ollama)
1. Ensure [Ollama](https://ollama.com) is running locally with a model pulled (e.g., `ollama pull llama3.2`).
2. Run the pipeline:
   `python3 run_pipeline.py`
3. Review the generated brief in `outputs/weekly_exec_brief.md`.
