import re

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

        paragraphs = self._split_into_paragraphs(text)
        chunks = []
        current_chunk = ""
        for paragraph in paragraphs:
            if len(current_chunk) + len(paragraph) <= chunk_size:
                current_chunk = self._join_text(
                    current_chunk,
                    paragraph
                )
            else:
                if current_chunk.strip():
                    chunks.append(current_chunk.strip())
                current_chunk = paragraph
        if current_chunk.strip():
            chunks.append(current_chunk.strip())
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

    def _split_into_paragraphs(
        self,
        text: str
    ) -> list[str]:
        
        text = text.replace("\r\n", "\n")
        raw_paragraphs = re.split(
            r"\n\s*\n",
            text
        )
        paragraphs = []

        for paragraph in raw_paragraphs:
            paragraph = self._clean_paragraph(paragraph)
            if paragraph:
                paragraphs.append(paragraph)
        return paragraphs

    def _clean_paragraph(
        self,
        paragraph: str
    ) -> str:
        
        paragraph = re.sub(
            r"\s+",
            " ",
            paragraph
        )
        return paragraph.strip()

    def _join_text(
        self,
        current_text: str,
        new_text: str
    ) -> str:

        if not current_text:
            return new_text
        return current_text + "\n\n" + new_text