
def chunk_text(text, chunk_size=500, overlap=100):
    """Split text into overlapping word-based chunks."""

    words = text.split()

    chunks = []

    start = 0

    while start < len(words):

        end = start + chunk_size

        chunk = " ".join(words[start:end])

        if chunk.strip():
            chunks.append(chunk)

        start += chunk_size - overlap

    return chunks


def chunk_documents(documents):
    """Create chunks while preserving document and page metadata."""

    all_chunks = []

    for document in documents:

        filename = document["filename"]

        for page in document["pages"]:

            page_chunks = chunk_text(page["text"])

            for chunk_number, content in enumerate(
                page_chunks,
                start=1
            ):

                all_chunks.append({
                    "filename": filename,
                    "page": page["page"],
                    "chunk_number": chunk_number,
                    "text": content
                })

    return all_chunks
