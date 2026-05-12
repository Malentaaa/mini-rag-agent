from app.parsers.pdf_parser import PDFParser
from app.rag.text_splitter import TextSplitter


parser = PDFParser()
splitter = TextSplitter()


text = parser.extract_text(
    "data/docs/Статистический_анализ_данных_Теория_вероятностей.pdf"
)

chunks = splitter.split_text(text)

print(f"Chunks count: {len(chunks)}")

print("\nFIRST CHUNK:\n")

print(chunks[0])

print("\nSECOND CHUNK:\n")

print(chunks[1])