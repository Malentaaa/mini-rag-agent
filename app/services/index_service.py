from pathlib import Path

from app.pipeline.indexing_pipeline import IndexingPipeline
from app.core.config import (
    DOCS_PATH,
    INDEX_PATH,
    CHUNKS_PATH
)
from app.core.logger import get_logger

logger = get_logger(__name__)

class IndexService:
    def __init__(self):
        self.pipeline = IndexingPipeline()

    def ensure_index_exists(self):
        index_exists = INDEX_PATH.exists()
        chunks_exist = CHUNKS_PATH.exists()
        if index_exists and chunks_exist:
            logger.info("Index found")
            return
        logger.info("Index not found")
        logger.info("Creating index")
        self.pipeline.run(
            docs_path=str(DOCS_PATH),
            index_path=str(INDEX_PATH),
            records_path=str(CHUNKS_PATH)
        )
        logger.info("Index created")