import pdfplumber
import fitz  # PyMuPDF
from docx import Document
from tempfile import NamedTemporaryFile

def extract_text_from_pdf(file):
    with pdfplumber.open(file.file) as pdf:
        return "\n".join(page.extract_text() for page in pdf.pages if page.extract_text())

def extract_text_from_docx(file):
    doc = Document(file.file)
    return "\n".join([p.text for p in doc.paragraphs])

def extract_text(file):
    if file.filename.endswith(".pdf"):
        return extract_text_from_pdf(file)
    elif file.filename.endswith(".docx"):
        return extract_text_from_docx(file)
    else:
        return "Unsupported file type"
