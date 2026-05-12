from app.rag.embedder import Embedder
from app.rag.index_store import IndexStore
from app.rag.retriever import Retriever


class QueryPipeline:
    def __init__(self):
        self.embedder = Embedder()
        self.store = IndexStore()

    def run(
        self,
        query: str,
        index_path: str,
        chunks_path: str,
        top_k: int = 3
    ):
        self.store.load_index(
            index_path
        )
        chunks = self.store.load_chunks(
            chunks_path
        )
        retriever = Retriever(
            embedder=self.embedder,
            index_store=self.store,
            chunks=chunks
        )
        results = retriever.retrieve(
            query=query,
            top_k=top_k
        )
        return results