from app.core.config import (
    CHUNK_SIZE,
    CHUNK_OVERLAP
)

class TextSplitter:

    def split_text(
        self,
        text: str,
        chunk_size: int = CHUNK_SIZE,
        overlap: int = CHUNK_OVERLAP
    ) -> list[str]:
        chunks = []
        start = 0
        while start < len(text):
            end = start + chunk_size
            chunk = text[start:end]
            if chunk.strip():
                chunks.append(chunk)
            start += chunk_size - overlap
        return chunks

    def split_pages(
        self,
        pages: list[dict]
    ) -> list[dict]:
        records = []
        for page_data in pages:
            chunks = self.split_text(
                page_data["text"]
            )
            for chunk in chunks:
                records.append(
                    {
                        "chunk": chunk,
                        "source": page_data["source"],
                        "page": page_data["page"]
                    }
                )
        return records