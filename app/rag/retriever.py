import faiss
import numpy as np

from app.core.config import TOP_K

class Retriever:

    def __init__(
        self,
        embedder,
        index_store,
        records
    ):
        self.embedder = embedder
        self.index = index_store.index
        self.records = records

    def retrieve(
        self,
        query: str,
        top_k: int = TOP_K
    ):
        query_embedding = self.embedder.encode(
            [query]
        )
        query_embedding = np.array(
            query_embedding
        ).astype("float32")
        faiss.normalize_L2(
            query_embedding
        )
        distances, indices = self.index.search(
            query_embedding,
            top_k
        )
        results = []
        for distance, idx in zip(distances[0], indices[0]):
            record = self.records[idx].copy()
            record["score"] = float(distance)
            results.append(record)
        return results