
import fitz
import os


def extract_text_from_pdf(file_path):
    """Extract text from every page of a PDF."""

    if not os.path.exists(file_path):
        raise FileNotFoundError(file_path)

    document = fitz.open(file_path)

    pages = []

    for page_number, page in enumerate(document, start=1):

        text = page.get_text("text")

        if text.strip():
            pages.append({
                "page": page_number,
                "text": text
            })

    document.close()

    return pages


def process_pdf_folder(folder_path="documents"):
    """Extract text from all PDFs in a folder."""

    all_documents = []

    for filename in os.listdir(folder_path):

        if filename.lower().endswith(".pdf"):

            file_path = os.path.join(
                folder_path,
                filename
            )

            pages = extract_text_from_pdf(file_path)

            all_documents.append({
                "filename": filename,
                "pages": pages
            })

    return all_documents
