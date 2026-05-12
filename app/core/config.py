from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent.parent
DOCS_PATH = BASE_DIR / "data" / "docs"
INDEX_PATH = BASE_DIR / "storage" / "indexes" / "faiss.index"
CHUNKS_PATH = BASE_DIR / "storage" / "indexes" / "chunks.pkl"