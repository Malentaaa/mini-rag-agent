from app.pipeline.indexing_pipeline import IndexingPipeline

pipeline = IndexingPipeline()

pipeline.run(
    docs_path="data/docs",
    index_path="storage/indexes/faiss.index",
    chunks_path="storage/indexes/chunks.pkl"
)