import fitz


class PDFParser:

    def extract_text(self, pdf_path: str) -> str:

        document = fitz.open(pdf_path)

        full_text = []

        for page in document:
            text = page.get_text()
            full_text.append(text)

        document.close()

        return "\n".join(full_text)