from fastapi import FastAPI
from fastapi import Request
from fastapi import Form

from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.api.rag_router import router
from app.services.index_service import IndexService
from app.services.rag_service import RAGService
from app.core.config import TOP_K


app = FastAPI(
    title="Mini RAG Agent"
)

app.include_router(router)

app.mount(
    "/static",
    StaticFiles(directory="app/static"),
    name="static"
)

templates = Jinja2Templates(
    directory="app/templates"
)

index_service = IndexService()
index_service.ensure_index_exists()
rag_service = RAGService()

@app.get("/", response_class=HTMLResponse)
def home(request: Request):

    return templates.TemplateResponse(
        request,
        "index.html",
        {
            "query": "",
            "top_k": TOP_K,
            "results": None
        }
    )
    
@app.post("/", response_class=HTMLResponse)
def ask(
    request: Request,
    query: str = Form(...),
    top_k: int = Form(5)
):
    results = rag_service.ask(
        query=query,
        top_k=top_k
    )
    return templates.TemplateResponse(
        request,
        "index.html",
        {
            "query": query,
            "top_k": top_k,
            "results": results
        }
    )