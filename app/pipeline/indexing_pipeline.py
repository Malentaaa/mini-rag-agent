from pathlib import Path

from app.parsers.pdf_parser import PDFParser
from app.rag.text_splitter import TextSplitter
from app.rag.embedder import Embedder
from app.rag.index_store import IndexStore
from app.core.logger import get_logger

logger = get_logger(__name__)

class IndexingPipeline:

    def __init__(self):
        self.parser = PDFParser()
        self.splitter = TextSplitter()
        self.embedder = Embedder()
        self.store = IndexStore()

    def run(
        self,
        docs_path: str,
        index_path: str,
        records_path: str
    ):

        all_records = []
        pdf_files = Path(docs_path).glob("*.pdf")
        for pdf_path in pdf_files:
            logger.info(f"Processing PDF: {pdf_path.name}")
            pages = self.parser.extract_pages(
                str(pdf_path)
            )
            records = self.splitter.split_pages(
                pages
            )
            all_records.extend(records)
        logger.info(f"Total records: {len(all_records)}")
        chunks = [
            record["chunk"]
            for record in all_records
        ]
        embeddings = self.embedder.encode(
            chunks
        )
        self.store.create_index(
            embeddings
        )
        self.store.save_index(
            index_path
        )
        self.store.save_records(
            all_records,
            records_path
        )
        logger.info("Index created")