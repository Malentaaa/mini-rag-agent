import json
from pathlib import Path

from app.pipeline.indexing_pipeline import IndexingPipeline

from app.core.config import (
    DOCS_PATH,
    INDEX_PATH,
    CHUNKS_PATH,
    INDEX_META_PATH,
    MODEL_NAME
)

from app.core.logger import get_logger

logger = get_logger(__name__)

class IndexService:
    
    def __init__(self):
        self.pipeline = IndexingPipeline()

    def ensure_index_exists(self):
        if self._index_is_actual():
            logger.info("Index found and actual")
            return

        logger.info("Index not found or outdated")
        logger.info("Rebuilding index...")
        self.pipeline.run(
            docs_path=str(DOCS_PATH),
            index_path=str(INDEX_PATH),
            records_path=str(CHUNKS_PATH)
        )
        self._save_index_meta()
        logger.info("Index rebuilt")

    def _index_is_actual(self) -> bool:
        if not INDEX_PATH.exists():
            return False
        if not CHUNKS_PATH.exists():
            return False
        if not INDEX_META_PATH.exists():
            return False

        saved_meta = self._load_index_meta()
        current_meta = self._build_current_meta()
        return saved_meta == current_meta

    def _build_current_meta(self) -> dict:
        pdf_files = sorted(
            DOCS_PATH.glob("*.pdf")
        )
        files = []
        for pdf_file in pdf_files:
            stat = pdf_file.stat()
            files.append(
                {
                    "name": pdf_file.name,
                    "size": stat.st_size,
                    "modified": stat.st_mtime
                }
            )

        return {
            "model_name": MODEL_NAME,
            "files": files
        }

    def _save_index_meta(self):
        meta = self._build_current_meta()
        with open(INDEX_META_PATH, "w", encoding="utf-8") as f:
            json.dump(
                meta,
                f,
                ensure_ascii=False,
                indent=4
            )
    def _load_index_meta(self) -> dict:
        with open(INDEX_META_PATH, "r", encoding="utf-8") as f:
            return json.load(f)