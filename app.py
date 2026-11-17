
import os
import requests
from dotenv import load_dotenv

load_dotenv()

OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL")
OLLAMA_EMBED_MODEL = os.getenv("OLLAMA_EMBED_MODEL")


def ask_ollama(question):
    response = requests.post(
        f"{OLLAMA_BASE_URL}/api/chat",
        json={
            "model": OLLAMA_MODEL,
            "messages": [
                {
                    "role": "user",
                    "content": question
                }
            ],
            "stream": False
        },
        timeout=(10, 300)
    )

    response.raise_for_status()

    return response.json()["message"]["content"]


def generate_embedding(text):
    response = requests.post(
        f"{OLLAMA_BASE_URL}/api/embed",
        json={
            "model": OLLAMA_EMBED_MODEL,
            "input": text
        },
        timeout=120
    )

    response.raise_for_status()

    return response.json()["embeddings"][0]


if __name__ == "__main__":
    print("Testing Ollama connection...")

    answer = ask_ollama(
        "Explain what Retrieval-Augmented Generation is in two sentences."
    )

    print("\nLLM Response:")
    print(answer)

    embedding = generate_embedding(
        "Artificial intelligence research"
    )

    print("\nEmbedding dimensions:", len(embedding))

    print("\nOllama integration successful!")
