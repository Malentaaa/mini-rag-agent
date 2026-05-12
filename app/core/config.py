from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent.parent
DOCS_PATH = BASE_DIR / "data" / "docs"
INDEX_PATH = BASE_DIR / "storage" / "indexes" / "faiss.index"
CHUNKS_PATH = BASE_DIR / "storage" / "indexes" / "chunks.pkl"
MODEL_NAME = "BAAI/bge-m3"
TOP_K = 5
CHUNK_SIZE = 500
CHUNK_OVERLAP = 100