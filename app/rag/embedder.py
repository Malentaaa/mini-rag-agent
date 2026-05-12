from sentence_transformers import SentenceTransformer
from app.core.config import MODEL_NAME

class Embedder:
    def __init__(self):
        self.model = SentenceTransformer(MODEL_NAME)

    def encode(
        self,
        texts: list[str]
    ):
        embeddings = self.model.encode(
            texts,
            show_progress_bar=True
        )
        return embeddings