import numpy as np
from app.core.config import TOP_K


class Retriever:
    def __init__(
        self,
        embedder,
        index_store,
        chunks
    ):
        self.embedder = embedder
        self.index = index_store.index
        self.chunks = chunks

    def retrieve(
        self,
        query: str,
        top_k: int = TOP_K
    ):
        query_embedding = self.embedder.encode(
            [query]
        )
        distances, indices = self.index.search(
            np.array(query_embedding).astype("float32"),
            top_k
        )
        results = []
        for idx in indices[0]:
            chunk = self.chunks[idx]
            results.append(chunk)
        return results