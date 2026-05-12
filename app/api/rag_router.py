from fastapi import APIRouter

from app.schemas.rag_schema import QueryRequest
from app.pipeline.query_pipeline import QueryPipeline
from app.core.config import (
    INDEX_PATH,
    CHUNKS_PATH
)

router = APIRouter()
pipeline = QueryPipeline()

@router.post("/ask")
def ask_question(
    request: QueryRequest
):
    results = pipeline.run(
        query=request.query,
        index_path=str(INDEX_PATH),
        chunks_path=str(CHUNKS_PATH),
        top_k=request.top_k
    )
    return {
        "query": request.query,
        "results": results
    }