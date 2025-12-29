import gradio as gr
import ollama
import json
from pathlib import Path

INTENT_FILE = Path("intents/test_intent.json")
CONTEXT_FILE = Path("output/retrieved_context.txt")

SYSTEM_PROMPT = """
You are a QA automation architect.

Return ONLY valid JSON.
Do not add explanations or markdown.

Schema:
{
  "feature": "Login",
  "tests": [
    {
      "name": "Valid Login",
      "type": "positive",
      "steps": [
        {"action": "goto", "value": "https://practicetestautomation.com/practice-test-login/"},
        {"action": "fill", "selector": "#username", "value": "student"},
        {"action": "fill", "selector": "#password", "value": "Password123"},
        {"action": "click", "selector": "#submit"}
      ],
      "expect": "User logged in"
    }
  ]
}
"""

def generate_intent(prompt: str) -> str:
    try:
        context = CONTEXT_FILE.read_text() if CONTEXT_FILE.exists() else ""

        response = ollama.chat(
            model="llama3.1:8b",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": context + "\n\n" + prompt}
            ]
        )

        raw = response["message"]["content"]
        intent = json.loads(raw)

        INTENT_FILE.parent.mkdir(parents=True, exist_ok=True)
        INTENT_FILE.write_text(json.dumps(intent, indent=2))

        return "✅ Test intent generated successfully.\n\nSaved to intents/test_intent.json"

    except Exception as e:
        return f"❌ ERROR:\n{str(e)}"

with gr.Blocks() as demo:
    gr.Markdown("# 🧪 GenAI QA Chatbot (RAG → Test Intent → Playwright)")
    gr.Markdown(
        "Generate dynamic test intent from requirements and drive Playwright automation."
    )

    prompt = gr.Textbox(
        label="Enter test generation prompt",
        lines=3,
        placeholder="Generate only positive login test cases"
    )

    output = gr.Markdown()

    with gr.Row():
        run = gr.Button("🚀 Generate Test Intent")
        clear = gr.Button("Clear")

    run.click(generate_intent, prompt, output)
    clear.click(lambda: "", None, output)

demo.launch()