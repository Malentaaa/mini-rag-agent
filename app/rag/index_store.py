import faiss
import pickle
import numpy as np

class IndexStore:

    def __init__(self):
        self.index = None

    def create_index(
        self,
        embeddings
    ):
        embeddings = np.array(embeddings).astype("float32")
        faiss.normalize_L2(embeddings)
        dimension = embeddings.shape[1]
        self.index = faiss.IndexFlatIP(dimension)
        self.index.add(embeddings)

    def save_index(
        self,
        index_path: str
    ):
        faiss.write_index(
            self.index,
            index_path
        )

    def load_index(
        self,
        index_path: str
    ):
        self.index = faiss.read_index(
            index_path
        )

    def save_records(
        self,
        records,
        records_path: str
    ):
        with open(records_path, "wb") as f:
            pickle.dump(records, f)

    def load_records(
        self,
        records_path: str
    ):
        with open(records_path, "rb") as f:
            records = pickle.load(f)
        return records