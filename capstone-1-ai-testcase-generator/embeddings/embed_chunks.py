from pathlib import Path
from sentence_transformers import SentenceTransformer
import json

def load_chunks(file_path: Path):
    if not file_path.exists():
        raise FileNotFoundError(f"Chunks file not found: {file_path}")
    content = file_path.read_text(encoding="utf-8")
    return content.split("\n\n---\n\n")

if __name__ == "__main__":
    # Resolve paths relative to THIS file
    BASE_DIR = Path(__file__).resolve().parent.parent
    OUTPUT_DIR = BASE_DIR / "output"

    chunks_file = OUTPUT_DIR / "chunks.txt"
    chunks = load_chunks(chunks_file)

    model = SentenceTransformer("all-MiniLM-L6-v2")
    embeddings = model.encode(chunks).tolist()

    vector_store = [
        {"id": idx, "text": chunk, "embedding": embedding}
        for idx, (chunk, embedding) in enumerate(zip(chunks, embeddings))
    ]

    output_file = OUTPUT_DIR / "vector_store.json"
    output_file.write_text(json.dumps(vector_store, indent=2), encoding="utf-8")

    print(f"✅ Stored {len(vector_store)} embeddings.")
    print(f"📦 Output: {output_file}")