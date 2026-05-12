from pydantic import BaseModel

from app.core.config import TOP_K

class QueryRequest(BaseModel):
    query: str
    top_k: int = TOP_K