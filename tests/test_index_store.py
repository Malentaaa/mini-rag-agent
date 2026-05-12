from app.parsers.pdf_parser import PDFParser
from app.rag.text_splitter import TextSplitter
from app.rag.embedder import Embedder
from app.rag.index_store import IndexStore


parser = PDFParser()
splitter = TextSplitter()
embedder = Embedder()
store = IndexStore()

text = parser.extract_text(
    "data/docs/Статистический_анализ_данных_Теория_вероятностей.pdf"
)

chunks = splitter.split_text(text)
embeddings = embedder.encode(chunks)
store.create_index(embeddings)

store.save_index(
    "storage/indexes/faiss.index"
)

store.save_chunks(
    chunks,
    "storage/indexes/chunks.pkl"
)

print("INDEX SAVED")
print(f"Chunks saved: {len(chunks)}")