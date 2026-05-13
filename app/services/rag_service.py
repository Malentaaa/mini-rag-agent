from app.pipeline.query_pipeline import QueryPipeline

from app.core.config import (
    INDEX_PATH,
    CHUNKS_PATH,
    TOP_K
)

class RAGService:
    def __init__(self):

        self.pipeline = QueryPipeline()

    def ask(
        self,
        query: str,
        top_k: int = TOP_K
    ):
        results = self.pipeline.run(
            query=query,
            index_path=str(INDEX_PATH),
            records_path=str(CHUNKS_PATH),
            top_k=top_k
        )
        return results