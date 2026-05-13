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
        records_path: str,
        top_k: int = 3
    ):
        self.store.load_index(
            index_path
        )
        records = self.store.load_records(
            records_path
        )
        retriever = Retriever(
            embedder=self.embedder,
            index_store=self.store,
            records=records
        )
        results = retriever.retrieve(
            query=query,
            top_k=top_k
        )
        return results