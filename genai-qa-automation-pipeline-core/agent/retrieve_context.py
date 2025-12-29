from pathlib import Path
from sentence_transformers import SentenceTransformer, util
import json

def load_vector_store(file_path: Path):
    if not file_path.exists():
        raise FileNotFoundError(f"Vector store not found: {file_path}")
    return json.loads(file_path.read_text(encoding="utf-8"))

if __name__ == "__main__":
    BASE_DIR = Path(__file__).resolve().parent.parent
    OUTPUT_DIR = BASE_DIR / "output"

    query = "Generate test cases for user login functionality"

    model = SentenceTransformer("all-MiniLM-L6-v2")
    query_embedding = model.encode(query)

    vector_store_file = OUTPUT_DIR / "vector_store.json"
    vector_store = load_vector_store(vector_store_file)

    embeddings = [item["embedding"] for item in vector_store]
    texts = [item["text"] for item in vector_store]

    scores = util.cos_sim(query_embedding, embeddings)[0]
    top_k = 3
    top_results = scores.topk(k=top_k)

    retrieved_context = [texts[idx] for idx in top_results.indices]

    output_file = OUTPUT_DIR / "retrieved_context.txt"
    output_file.write_text("\n\n".join(retrieved_context), encoding="utf-8")

    print("✅ Retrieved context saved.")
    print(f"📄 Output: {output_file}")