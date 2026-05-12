from app.pipeline.query_pipeline import QueryPipeline

pipeline = QueryPipeline()

query = "пересекающиеся события"


results = pipeline.run(
    query=query,
    index_path="storage/indexes/faiss.index",
    chunks_path="storage/indexes/chunks.pkl",
    top_k=3
)

for i, chunk in enumerate(results):
    print(f"\nRESULT {i+1}:\n")
    print(chunk[:1000])