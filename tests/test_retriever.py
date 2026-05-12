from app.parsers.pdf_parser import PDFParser
from app.rag.text_splitter import TextSplitter
from app.rag.embedder import Embedder
from app.rag.index_store import IndexStore
from app.rag.retriever import Retriever


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

retriever = Retriever(
    embedder=embedder,
    index_store=store,
    chunks=chunks
)

query = "Что такое вероятностное пространство?"

results = retriever.retrieve(
    query=query,
    top_k=3
)

for i, chunk in enumerate(results):
    print(f"\nRESULT {i+1}:\n")
    print(chunk[:1000])