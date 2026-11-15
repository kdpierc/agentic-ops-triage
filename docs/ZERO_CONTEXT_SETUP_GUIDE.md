# Zero-Context Setup Guide: Build & Publish a Multi-Agent AI Pipeline

**What you are building:** A multi-agent AI system on your Mac that classifies operational incident tickets, detects systemic risks, and generates an executive summary—published cleanly to GitHub.  
**Safety guarantee:** Everything happens inside one isolated project folder (`~/Developer/agentic-ops-triage`). You cannot break your Mac or VS Code.

---

## Step 1: Create Your Project Folder & Empty Files (1 Minute)

1. Open **VS Code** on your Mac.
2. Open the built-in terminal panel at the bottom of VS Code by pressing **`Control` and `~` together** (the squiggly key above `Tab`). *(Or click **Terminal -> New Terminal** in the top Mac menu bar.)*
3. Copy the commands below, paste them into that bottom terminal area, and press **`Return` / `Enter`**:

    mkdir -p ~/Developer/agentic-ops-triage/{agents,data,docs,outputs}
    cd ~/Developer/agentic-ops-triage
    git init
    touch README.md ARCHITECTURE.md run_pipeline.py .gitignore
    touch agents/01_triage_agent.md agents/02_risk_agent.md agents/03_exec_brief_agent.md
    touch data/synthetic_incidents.json
    code -r .

4. **What you should see:** VS Code refreshes, and the **Explorer** sidebar on the left shows **`AGENTIC-OPS-TRIAGE`** at the top with 4 folders (`agents`, `data`, `docs`, `outputs`) and 4 files (`.gitignore`, `ARCHITECTURE.md`, `README.md`, `run_pipeline.py`) underneath it.
5. **Click "Trust":** If a banner appears at the top asking *"Do you trust the authors of the files in this folder?"*, click **Manage** -> click **Trust** (or **Yes, I trust the authors**).

---

## Step 2: Fill Out Your 8 Project Files (Top-to-Bottom in Sidebar Order)

Look at the **Explorer** sidebar on the left side of VS Code:
1. Click the little **`>`** arrow next to the **`agents`** folder so you can see the 3 files inside it.
2. Click the little **`>`** arrow next to the **`data`** folder so you can see the file inside it.

Work straight down the sidebar from top to bottom. **For every file below:**
* **Click** the filename in the left sidebar to open it in the center editor. *(If a file already has text in it, press **`Command` and `A` together**, then press **`Delete`** so you start with a blank page.)*
* **Copy** the block underneath that filename and **paste** it (**`Command` and `V` together**) into the blank page.
* **Save** by pressing **`Command` and `S` together** (do not press the `+` key, which zooms your font in).
* **How to verify it saved:** Look at the file's tab at the top of the editor. While unsaved, a **solid white dot (`●`)** appears next to the filename. Once saved, the white dot disappears and turns into an **`×`**. *(Note: A green **`U`** next to the filename simply stands for "Untracked by Git yet"—that is completely normal until Step 4.)*

### File 1 of 8: `agents` -> `01_triage_agent.md`
Click **`01_triage_agent.md`**, paste this inside, and press **`Command` and `S` together**:

    # Agent 1: Incident Classification & Pattern Extractor

    ## Objective
    Analyze raw operational incident records and group them by root-cause domain, severity, and affected service layer.

    ## Guardrails
    - Never invent root causes not explicitly supported by the ticket description.
    - Flag any incident with < 0.80 confidence for Human-in-the-Loop (HITL) review.

    ## Output Format (Strict JSON)
    Return a JSON list where each item follows this exact schema:
    {
      "incident_id": "",
      "category": "",
      "severity": "Low | Medium | High | Critical",
      "confidence": 0.0,
      "requires_hitl": false
    }

### File 2 of 8: `agents` -> `02_risk_agent.md`
Click **`02_risk_agent.md`**, paste this inside, and press **`Command` and `S` together**:

    # Agent 2: Ecosystem & Dependency Risk Analyzer

    ## Objective
    Review the structured incident classifications from Agent 1 and identify systemic patterns, recurring backend bottlenecks, and downstream operational risks across facilities.

    ## Analysis Rules
    1. Group incidents that share a common upstream service, integration point, or failure mode.
    2. Highlight any pattern occurring 2 or more times as a **Systemic Trend** rather than an isolated defect.
    3. Separate incidents flagged `requires_hitl: true` into an **Unverified / Needs Human Triage** section so uncertain classifications do not skew risk scoring.

    ## Output Format (Markdown)
    - **Systemic Trends Detected** (Pattern, Affected Service/Sites, Operational Impact)
    - **Downstream Dependency Risks**
    - **Items Held for Human-in-the-Loop Verification**

### File 3 of 8: `agents` -> `03_exec_brief_agent.md`
Click **`03_exec_brief_agent.md`**, paste this inside, and press **`Command` and `S` together**:

    # Agent 3: Executive Telemetry Synthesizer

    ## Objective
    Translate technical incident patterns and dependency risks into a concise, decision-ready weekly brief for VP/SVP operations and engineering leadership.

    ## Guardrails & Tone
    - Lead with business and operational impact, not raw log jargon.
    - Every recommended action must tie directly to a documented pattern from Agent 2.
    - Keep the brief scannable in under 2 minutes.

    ## Output Format (Markdown)
    ### Weekly Operational Health & Risk Brief
    1. **Executive Headline** (2–3 sentences summarizing overall platform stability and top risk)
    2. **Top Priority Interventions** (Ranked table: Issue | Operational Impact | Recommended Owner/Action)
    3. **Watchlist & Human-Review Queue** (Emerging trends or low-confidence items under investigation)

### File 4 of 8: `data` -> `synthetic_incidents.json`
Click **`synthetic_incidents.json`**, paste this inside, and press **`Command` and `S` together**:

    [
      {
        "incident_id": "INC-1041",
        "facility": "DC-North-04",
        "service": "Inventory-Sync-API",
        "summary": "Batch inventory reconciliation timed out after 30s during peak shift handoff, delaying pallet receiving scans for 45 minutes."
      },
      {
        "incident_id": "INC-1042",
        "facility": "DC-Midwest-11",
        "service": "Inventory-Sync-API",
        "summary": "Duplicate ASN payload caused Inventory-Sync-API retry storm and stalled outbound dock door assignment."
      },
      {
        "incident_id": "INC-1043",
        "facility": "DC-South-02",
        "service": "Label-Print-Service",
        "summary": "Zebra printer firmware mismatch after overnight patch caused intermittent barcode formatting errors on cold-chain lanes."
      },
      {
        "incident_id": "INC-1044",
        "facility": "DC-West-09",
        "service": "Access-Portal-Auth",
        "summary": "Temporary contractor badge provisioning failed role-mapping sync; resolved via self-service directory refresh."
      },
      {
        "incident_id": "INC-1045",
        "facility": "DC-East-07",
        "service": "Unknown-Telemetry",
        "summary": "Intermittent scanner lag reported by floor supervisor; network packet logs inconclusive."
      }
    ]

### File 5 of 8: `.gitignore`
*(Skip the `docs` and `outputs` folders—they stay empty for now.)*  
Click **`.gitignore`**, paste this inside, and press **`Command` and `S` together**:

    .DS_Store
    __pycache__/
    *.pyc
    .env
    .venv/

### File 6 of 8: `ARCHITECTURE.md`
Click **`ARCHITECTURE.md`**, paste this inside, and press **`Command` and `S` together**:

    # System Architecture & Responsible AI Guardrails

    ## End-to-End Workflow

    ```mermaid
    flowchart LR
        A[Raw Incident Telemetry] --> B[Agent 1: Classifier & Confidence Scorer]
        B -->|Confidence < 0.80| C[Human-in-the-Loop Queue]
        B -->|Confidence >= 0.80| D[Agent 2: Ecosystem & Dependency Risk]
        D --> E[Agent 3: Executive Brief Synthesizer]
        E --> F[VP/SVP Weekly Decision Brief]
    ```

    ## Architectural Trade-Offs (Tool-Agnostic Design)
    - **Decoupled Prompts (`agents/*.md`):** Separating agent instructions from orchestration code allows non-engineering domain experts to audit and refine business rules without touching Python.
    - **Confidence Gating:** Enforcing a strict `0.80` confidence threshold prevents low-certainty classifications or silent hallucinations from skewing executive reporting.
    - **Model Portability:** The orchestration layer communicates via standard JSON payloads, allowing the underlying LLM runtime (local Ollama or enterprise API) to be swapped without rewriting agent rules.

### File 7 of 8: `README.md`
Click **`README.md`**, paste this inside, and press **`Command` and `S` together**:

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
    2. Run the pipeline: `python3 run_pipeline.py`
    3. Review the generated brief in `outputs/weekly_exec_brief.md`.

### File 8 of 8: `run_pipeline.py`
Click **`run_pipeline.py`**, paste this inside, and press **`Command` and `S` together**:

    import json
    import urllib.request
    from pathlib import Path

    OLLAMA_URL = "http://localhost:11434/api/generate"
    MODEL = "llama3.2"  # Replace with any local model installed in Ollama (e.g., mistral, qwen2.5)


    def load_text(path: str) -> str:
        return Path(path).read_text(encoding="utf-8")


    def call_local_agent(system_prompt: str, user_payload: str) -> str:
        prompt = f"{system_prompt}\n\n---\nINPUT DATA:\n{user_payload}"
        req_data = json.dumps(
            {"model": MODEL, "prompt": prompt, "stream": False}
        ).encode("utf-8")
        req = urllib.request.Request(
            OLLAMA_URL, data=req_data, headers={"Content-Type": "application/json"}
        )
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read().decode("utf-8"))["response"]


    def main():
        incidents = load_text("data/synthetic_incidents.json")

        print("Running Agent 1: Triage & Classification...")
        triage_instructions = load_text("agents/01_triage_agent.md")
        triage_results = call_local_agent(triage_instructions, incidents)

        print("Running Agent 2: Ecosystem & Dependency Risk...")
        risk_instructions = load_text("agents/02_risk_agent.md")
        risk_analysis = call_local_agent(risk_instructions, triage_results)

        print("Running Agent 3: Executive Telemetry Brief...")
        exec_instructions = load_text("agents/03_exec_brief_agent.md")
        exec_brief = call_local_agent(exec_instructions, risk_analysis)

        output_file = Path("outputs/weekly_exec_brief.md")
        output_file.write_text(exec_brief, encoding="utf-8")
        print(f"Pipeline complete. Brief saved to {output_file}")


    if __name__ == "__main__":
        main()

**Checkpoint:** Look at all open file tabs across the top of VS Code. Every single tab should have an **`×`** next to the filename and **zero solid white dots (`●`)**.

---

## Step 3: Set Up Local AI (Ollama) & Run Your Pipeline

1. Open the bottom terminal inside VS Code (**`Control` and `~` together**).
2. *(One-time setup if Ollama isn't installed yet)* Install and start Ollama:

    brew install --cask ollama
    open -a Ollama

   *(Wait 5 seconds for the llama icon to appear in your Mac's top menu bar.)*
3. Download the local model and execute your pipeline:

    ollama pull llama3.2
    python3 run_pipeline.py

4. **What you should see:** The terminal prints `Running Agent 1...`, `Running Agent 2...`, `Running Agent 3...`, and `Pipeline complete. Brief saved to outputs/weekly_exec_brief.md`. Click **`outputs`** -> **`weekly_exec_brief.md`** in your left sidebar to inspect your generated executive brief.

---

## Step 4: Publish Your Project & Sample Output to GitHub

1. **Create a standardized repository on GitHub:**
   * Open your web browser and go to **github.com/new**.
   * In **Repository name**, type: `agentic-ops-triage`
   * **Standardization Best Practice — Always Add a Description:** Paste a clear, one-line executive summary into the **Description** field so your portfolio stays uniform and easy to scan (e.g., *"Tool-agnostic multi-agent pipeline for incident triage, ecosystem risk analysis, and executive telemetry reporting with HITL confidence guardrails."*).
   * Leave the visibility set to **Public**.
   * **Important:** Leave *"Add a README file"*, *".gitignore"*, and *"Choose a license"* **UNCHECKED** (because you already created them in Step 2).
   * Click the green **Create repository** button and ignore the setup instructions on the next screen.
2. **Push your local files (including your sample output) to GitHub:**
   * Return to VS Code's bottom terminal (**`Control` and `~` together**).
   * Copy the lines below, paste them into the terminal, and press **`Return` / `Enter`** *(mentees: replace `YOUR_USERNAME` with your own GitHub username)*:

    git add .
    git commit -m "feat: initial multi-agent incident triage and telemetry pipeline"
    git branch -M main
    git remote add origin https://github.com/YOUR_USERNAME/agentic-ops-triage.git
    git push -u origin main

3. **What you should see:** Refresh your GitHub page in your browser (`Command` and `R` together). All folders (`agents`, `data`, `docs`, `outputs`) and files will appear, `README.md` will render cleanly at the bottom, and the green `U` letters in VS Code will disappear.
4. **Optional Polish:** Click the gear icon next to **About** on the right side of your GitHub page to add 3–5 topic tags (such as `agentic-ai`, `systems-architecture`, `python`, `operations`, `human-in-the-loop`), and click **Pin** at the top right to feature it on your profile.

---

## Daily Muscle-Memory Cheat Sheet (5 Commands)

| Goal | Command |
| :--- | :--- |
| **Run your pipeline** | `python3 run_pipeline.py` |
| **Stage saved changes** | `git add .` |
| **Commit snapshot** | `git commit -m "feat: describe what changed"` |
| **Publish to GitHub** | `git push` |
| **Clear terminal text** | `clear` |
