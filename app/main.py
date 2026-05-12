from fastapi import FastAPI

from app.api.rag_router import router
from app.services.index_service import IndexService

app = FastAPI(
    title="Mini RAG Agent"
)

index_service = IndexService()
index_service.ensure_index_exists()

app.include_router(router)