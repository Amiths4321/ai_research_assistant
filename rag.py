
from vector_store import search_chunks
from app import ask_ollama


def answer_from_documents(question, top_k=5):
    """Answer questions using retrieved PDF content."""

    # Step 1: Retrieve relevant document chunks
    results = search_chunks(
        question,
        top_k=top_k
    )

    documents = results.get("documents", [[]])[0]
    metadatas = results.get("metadatas", [[]])[0]

    if not documents:
        return "I couldn't find relevant information in the uploaded documents."

    # Step 2: Build context with source information
    context_parts = []

    for document, metadata in zip(documents, metadatas):
        context_parts.append(
            f"""
Source: {metadata['filename']}
Page: {metadata['page']}

Content:
{document}
"""
        )

    context = "\n\n".join(context_parts)

    # Step 3: Ask the LLM to answer using retrieved context
    prompt = f"""
You are an AI research assistant.

Answer the user's question using ONLY the supplied document context.

Rules:
1. Do not invent facts.
2. If the answer is not in the context, say so.
3. Cite sources using filename and page number.
4. Distinguish evidence from interpretation.
5. Give a clear and structured answer.

DOCUMENT CONTEXT:
{context}

USER QUESTION:
{question}

Provide your answer with citations.
"""

    answer = ask_ollama(prompt)

    return answer


if __name__ == "__main__":

    question = input("Ask a question about your research papers: ")

    answer = answer_from_documents(question)

    print("\nRESEARCH ANSWER\n")
    print(answer)
