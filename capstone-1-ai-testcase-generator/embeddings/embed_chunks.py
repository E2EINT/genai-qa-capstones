from pathlib import Path
from sentence_transformers import SentenceTransformer
import json

def load_chunks(file_path: Path):
    content = file_path.read_text(encoding="utf-8")
    return content.split("\n\n---\n\n")

if __name__ == "__main__":
    model = SentenceTransformer("all-MiniLM-L6-v2")

    chunks_file = Path("../output/chunks.txt")
    chunks = load_chunks(chunks_file)

    embeddings = model.encode(chunks).tolist()

    vector_store = [
        {"id": idx, "text": chunk, "embedding": embedding}
        for idx, (chunk, embedding) in enumerate(zip(chunks, embeddings))
    ]

    output_file = Path("../output/vector_store.json")
    output_file.write_text(json.dumps(vector_store, indent=2), encoding="utf-8")

    print(f"Stored {len(vector_store)} embeddings successfully.")
