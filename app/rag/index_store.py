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

        dimension = embeddings.shape[1]
        self.index = faiss.IndexFlatL2(dimension)
        self.index.add(
            np.array(embeddings).astype("float32")
        )

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

    def save_chunks(
        self,
        chunks,
        chunks_path: str
    ):
        with open(chunks_path, "wb") as f:
            pickle.dump(chunks, f)

    def load_chunks(
        self,
        chunks_path: str
    ):
        with open(chunks_path, "rb") as f:
            chunks = pickle.load(f)
        return chunks