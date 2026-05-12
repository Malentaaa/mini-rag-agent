from app.parsers.pdf_parser import PDFParser
from app.rag.text_splitter import TextSplitter
from app.rag.embedder import Embedder


parser = PDFParser()
splitter = TextSplitter()
embedder = Embedder()

text = parser.extract_text(
    "data/docs/Статистический_анализ_данных_Теория_вероятностей.pdf"
)

chunks = splitter.split_text(text)

embeddings = embedder.encode(chunks)


print(f"Chunks count: {len(chunks)}")

print(f"Embeddings shape: {embeddings.shape}")

print("\nFIRST EMBEDDING:\n")

print(embeddings[0])