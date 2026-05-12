from pathlib import Path

from app.parsers.pdf_parser import PDFParser
from app.rag.text_splitter import TextSplitter
from app.rag.embedder import Embedder
from app.rag.index_store import IndexStore


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
        chunks_path: str
    ):
        all_chunks = []
        pdf_files = Path(docs_path).glob("*.pdf")
        for pdf_path in pdf_files:
            print(f"\nPROCESSING: {pdf_path.name}")
            text = self.parser.extract_text(
                str(pdf_path)
            )
            chunks = self.splitter.split_text(text)
            all_chunks.extend(chunks)
        print(f"\nTOTAL CHUNKS: {len(all_chunks)}")
        
        embeddings = self.embedder.encode(
            all_chunks
        )
        self.store.create_index(
            embeddings
        )
        self.store.save_index(
            index_path
        )
        self.store.save_chunks(
            all_chunks,
            chunks_path
        )
        print("\nINDEX CREATED")