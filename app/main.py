from fastapi import FastAPI
from fastapi import Request
from fastapi import Form
from pathlib import Path

from fastapi.responses import HTMLResponse, FileResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.api.rag_router import router
from app.services.index_service import IndexService
from app.services.rag_service import RAGService
from app.core.config import TOP_K
from app.services.page_preview_service import (
    PagePreviewService
)


app = FastAPI(
    title="Mini RAG Agent"
)

app.include_router(router)

app.mount(
    "/static",
    StaticFiles(directory="app/static"),
    name="static"
)

app.mount(
    "/docs-storage",
    StaticFiles(directory="data/docs"),
    name="docs-storage"
)

templates = Jinja2Templates(
    directory="app/templates"
)

index_service = IndexService()
index_service.ensure_index_exists()
rag_service = RAGService()
page_preview_service = PagePreviewService()


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

    pages = {}

    for result in results:

        key = (
            result["source"],
            result["page"]
        )

        if key not in pages:

            pages[key] = {
                "source": result["source"],
                "source_name": Path(result["source"]).name,
                "page": result["page"],
                "score": result.get("score")
            }

    page_results = list(pages.values())

    return templates.TemplateResponse(
        request,
        "index.html",
        {
            "query": query,
            "top_k": top_k,
            "results": page_results
        }
    )

@app.get("/page-preview")
def page_preview(
    source: str,
    page: int
):

    image_stream = (
        page_preview_service.render_page(
            pdf_path=source,
            page_number=page
        )
    )

    return StreamingResponse(
        image_stream,
        media_type="image/png"
    )