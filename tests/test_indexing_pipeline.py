from app.pipeline.indexing_pipeline import IndexingPipeline
from app.core.config import (
    DOCS_PATH,
    INDEX_PATH,
    CHUNKS_PATH
)

pipeline = IndexingPipeline()

pipeline.run(
    docs_path=str(DOCS_PATH),
    index_path=str(INDEX_PATH),
    chunks_path=str(CHUNKS_PATH) 
)