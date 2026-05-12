from app.pipeline.query_pipeline import QueryPipeline
from app.core.config import (
    INDEX_PATH,
    CHUNKS_PATH
)

pipeline = QueryPipeline()

query = "пересекающиеся события"


results = pipeline.run(
    query=query,
    index_path=str(INDEX_PATH),
    chunks_path=str(CHUNKS_PATH),
    top_k=3
)

for i, chunk in enumerate(results):
    print(f"\nRESULT {i+1}:\n")
    print(chunk[:1000])