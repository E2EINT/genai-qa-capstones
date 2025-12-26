import gradio as gr
import ollama
from pathlib import Path

RETRIEVED_CONTEXT_PATH = Path("output/retrieved_context.txt")

def chat_with_llm(user_input):
    # Load RAG context
    if RETRIEVED_CONTEXT_PATH.exists():
        context = RETRIEVED_CONTEXT_PATH.read_text(encoding="utf-8")
    else:
        context = "No retrieved context available."

    messages = [
        {
            "role": "system",
            "content": (
            "You are an AI assistant with two modes:\n"
            "1. If the question relates to software requirements or QA, generate structured test cases.\n"
            "2. If the question is general knowledge, answer it normally.\n"
            "Always prioritize QA context when available."
            )
        },
        {
            "role": "user",
            "content": f"Context:\n{context}\n\nQuestion:\n{user_input}"
        }
    ]

    response = ollama.chat(
        model="llama3.1:8b",
        messages=messages
    )

    return response["message"]["content"]

demo = gr.Interface(
    fn=chat_with_llm,
    inputs=gr.Textbox(
        label="Ask a QA question",
        placeholder="Generate test cases for login functionality",
        lines=6,          # 👈 height of input box
        max_lines=12      # 👈 auto-grow
    ),
    outputs=gr.Textbox(label="LLM Response",

        lines=15,          # 👈 height of input box
        max_lines=30      # 👈 auto-grow
    ),
        title="🧪 GenAI QA Chatbot (RAG + Local LLM)",
        description="PDF → RAG → Local LLM (Ollama) → Test Case Generation"
)

demo.launch()