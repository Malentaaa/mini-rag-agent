from fastapi import FastAPI

from app.api.rag_router import router

app = FastAPI(
    title="Mini RAG Agent"
)
app.include_router(router)