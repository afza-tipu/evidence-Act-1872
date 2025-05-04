import pdfplumber
import os

# File paths
INPUT_PDF = "../docs/pdf/evidence-act-1872.pdf"
OUTPUT_MD = "../docs/markdown/evidence-act-1872.md"

def pdf_to_markdown(pdf_path, output_path):
    print(f"🔍 Reading from: {pdf_path}")
    try:
        with pdfplumber.open(pdf_path) as pdf:
            full_text = ''
            for i, page in enumerate(pdf.pages):
                text = page.extract_text()
                if text:
                    full_text += f"\n\n<!-- Page {i + 1} -->\n\n" + text
        with open(output_path, "w", encoding="utf-8") as md_file:
            md_file.write("# Evidence Act, 1872\n\n")
            md_file.write("_Digitally converted from original PDF_\n\n")
            md_file.write(full_text)
        print(f"✅ Markdown saved to: {output_path}")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    os.makedirs(os.path.dirname(OUTPUT_MD), exist_ok=True)
    pdf_to_markdown(INPUT_PDF, OUTPUT_MD)
