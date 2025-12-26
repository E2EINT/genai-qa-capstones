from pathlib import Path
import PyPDF2

def extract_text_from_pdf(pdf_path: Path) -> str:
    if not pdf_path.exists():
        raise FileNotFoundError(f"PDF not found at: {pdf_path}")

    text = ""
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text


if __name__ == "__main__":
    # Resolve paths relative to THIS file (robust)
    BASE_DIR = Path(__file__).resolve().parent.parent
    DATA_DIR = BASE_DIR / "data"
    OUTPUT_DIR = BASE_DIR / "output"

    # 🔽 CHANGE ONLY THIS LINE IF NEEDED
    pdf_file = DATA_DIR / "sample-requirements.pdf"

    extracted_text = extract_text_from_pdf(pdf_file)

    output_file = OUTPUT_DIR / "requirements_text.txt"
    output_file.write_text(extracted_text, encoding="utf-8")

    print("✅ PDF text extracted successfully.")
    print(f"📄 Source: {pdf_file}")
    print(f"📝 Output: {output_file}")