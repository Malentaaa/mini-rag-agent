from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent.parent
DOCS_PATH = BASE_DIR / "data" / "docs"
INDEX_PATH = BASE_DIR / "storage" / "indexes" / "faiss.index"
INDEX_META_PATH = BASE_DIR / "storage" / "indexes" / "index_meta.json"
CHUNKS_PATH = BASE_DIR / "storage" / "indexes" / "records.pkl"
LOGS_DIR = BASE_DIR / "logs"
LOG_FILE = LOGS_DIR / "app.log"
MODEL_NAME = "BAAI/bge-m3"
TOP_K = 5
CHUNK_SIZE = 500
CHUNK_OVERLAP = 100