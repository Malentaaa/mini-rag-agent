import io
import fitz

class PagePreviewService:

    def render_page(
        self,
        pdf_path: str,
        page_number: int
    ):
        document = fitz.open(pdf_path)
        page = document.load_page(
            page_number - 1
        )
        pix = page.get_pixmap(
            matrix=fitz.Matrix(2, 2)
        )
        image_bytes = pix.tobytes("png")
        document.close()
        return io.BytesIO(image_bytes)