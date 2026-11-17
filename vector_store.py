
import os
import chromadb
import requests
from dotenv import load_dotenv

load_dotenv()

OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL")
EMBED_MODEL = os.getenv("OLLAMA_EMBED_MODEL")

DATA_DIR = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "data"
)

os.makedirs(DATA_DIR, exist_ok=True)

client = chromadb.PersistentClient(
    path=os.path.join(DATA_DIR, "chroma_db")
)

collection = client.get_or_create_collection(
    name="research_documents"
)


def generate_embedding(text):
    response = requests.post(
        f"{OLLAMA_BASE_URL}/api/embed",
        json={
            "model": EMBED_MODEL,
            "input": text
        },
        timeout=120
    )

    response.raise_for_status()

    return response.json()["embeddings"][0]


def store_chunks(chunks):
    for index, chunk in enumerate(chunks):

        embedding = generate_embedding(
            chunk["text"]
        )

        chunk_id = (
            f"{chunk['filename']}_"
            f"{chunk['page']}_"
            f"{chunk['chunk_number']}"
        )

        collection.upsert(
            ids=[chunk_id],
            embeddings=[embedding],
            documents=[chunk["text"]],
            metadatas=[{
                "filename": chunk["filename"],
                "page": chunk["page"],
                "chunk_number": chunk["chunk_number"]
            }]
        )

    return len(chunks)


def search_chunks(question, top_k=5):
    query_embedding = generate_embedding(question)

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    return results
