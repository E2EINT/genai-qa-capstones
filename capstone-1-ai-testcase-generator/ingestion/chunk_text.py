from pathlib import Path
from typing import List

def chunk_text(text: str, chunk_size: int = 500, overlap: int = 50) -> List[str]:
    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        start = end - overlap

    return chunks


if __name__ == "__main__":
    # Resolve paths relative to THIS file (robust)
    BASE_DIR = Path(__file__).resolve().parent.parent
    OUTPUT_DIR = BASE_DIR / "output"

    input_file = OUTPUT_DIR / "requirements_text.txt"

    if not input_file.exists():
        raise FileNotFoundError(f"Input file not found: {input_file}")

    text = input_file.read_text(encoding="utf-8")

    chunks = chunk_text(text)

    output_file = OUTPUT_DIR / "chunks.txt"
    output_file.write_text("\n\n---\n\n".join(chunks), encoding="utf-8")

    print(f"✅ Created {len(chunks)} text chunks.")
    print(f"📝 Input: {input_file}")
    print(f"📦 Output: {output_file}")