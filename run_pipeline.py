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
