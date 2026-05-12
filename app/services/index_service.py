from pathlib import Path

from app.pipeline.indexing_pipeline import IndexingPipeline
from app.core.config import (
    DOCS_PATH,
    INDEX_PATH,
    CHUNKS_PATH
)

class IndexService:
    def __init__(self):
        self.pipeline = IndexingPipeline()

    def ensure_index_exists(self):
        index_exists = Path(INDEX_PATH).exists()
        chunks_exist = Path(CHUNKS_PATH).exists()
        if index_exists and chunks_exist:
            print("\nINDEX FOUND")
            return
        print("\nINDEX NOT FOUND")
        print("CREATING INDEX...")
        self.pipeline.run(
            docs_path=str(DOCS_PATH),
            index_path=str(INDEX_PATH),
            chunks_path=str(CHUNKS_PATH)
        )
        print("\nINDEX CREATED")