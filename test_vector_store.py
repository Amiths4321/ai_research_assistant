
from vector_store import store_chunks, search_chunks


def test_vector_search():

    chunks = [
        {
            "filename": "paper1.pdf",
            "page": 1,
            "chunk_number": 1,
            "text": "Retrieval augmented generation combines language models with external knowledge retrieval."
        },
        {
            "filename": "paper2.pdf",
            "page": 3,
            "chunk_number": 1,
            "text": "Neural networks learn representations through training on large datasets."
        }
    ]

    stored = store_chunks(chunks)

    assert stored == 2

    results = search_chunks(
        "How does retrieval augmented generation work?",
        top_k=2
    )

    assert len(results["ids"][0]) > 0

    print("Vector search successful!")
    print(results["documents"])
