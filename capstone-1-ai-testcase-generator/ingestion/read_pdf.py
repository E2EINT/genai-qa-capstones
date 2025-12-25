from pathlib import Path
import PyPDF2

def extract_text_from_pdf(pdf_path: Path) -> str:
    text = ""
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text() + "\n"
    return text


if __name__ == "__main__":
    pdf_file = Path("../data/ShopEasy E-commerce Platform - Requirements Specification.pdf")
    extracted_text = extract_text_from_pdf(pdf_file)

    output_file = Path("../output/requirements_text.txt")
    output_file.write_text(extracted_text, encoding="utf-8")

    print("PDF text extracted successfully.")
