from app.parsers.pdf_parser import PDFParser


parser = PDFParser()

text = parser.extract_text("data/docs/Статистический_анализ_данных_Теория_вероятностей.pdf")

print(text[:3000])