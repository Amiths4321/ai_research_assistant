
from pdf_processor import extract_text_from_pdf
from chunking import chunk_text
from vector_store import store_chunks


def ingest_pdf(file_path):
    """Extract, chunk, and index a PDF."""

    import os

    filename = os.path.basename(file_path)

    print(f"Processing: {filename}")

    # Step 1: Extract PDF text
    pages = extract_text_from_pdf(file_path)

    if not pages:
        raise ValueError(
            f"No extractable text found in {filename}"
        )

    # Step 2: Split text into chunks
    chunks = []

    for page in pages:

        page_chunks = chunk_text(page["text"])

        for chunk_number, text in enumerate(
            page_chunks,
            start=1
        ):

            chunks.append({
                "filename": filename,
                "page": page["page"],
                "chunk_number": chunk_number,
                "text": text
            })

    if not chunks:
        raise ValueError("No document chunks were generated.")

    # Step 3: Generate embeddings and store in ChromaDB
    stored_count = store_chunks(chunks)

    print(f"Pages processed: {len(pages)}")
    print(f"Chunks stored: {stored_count}")

    return {
        "filename": filename,
        "pages": len(pages),
        "chunks": stored_count
    }


if __name__ == "__main__":

    result = ingest_pdf(
        "documents/research_paper.pdf"
    )

    print("\nIngestion completed!")
    print(result)
