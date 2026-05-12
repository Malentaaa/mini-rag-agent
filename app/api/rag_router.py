from fastapi import APIRouter

from app.schemas.rag_schema import QueryRequest
from app.pipeline.query_pipeline import QueryPipeline

router = APIRouter()
pipeline = QueryPipeline()

@router.post("/ask")
def ask_question(
    request: QueryRequest
):
    results = pipeline.run(
        query=request.query,
        index_path="storage/indexes/faiss.index",
        chunks_path="storage/indexes/chunks.pkl",
        top_k=request.top_k
    )
    return {
        "query": request.query,
        "results": results
    }