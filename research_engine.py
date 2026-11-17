
from rag import answer_from_documents
from web_search import search_web
from app import ask_ollama


def conduct_research(question):
    """Research a question using PDFs and web search."""

    print("Searching uploaded documents...")

    try:
        document_answer = answer_from_documents(
            question,
            top_k=5
        )
    except Exception as error:
        document_answer = f"Document search unavailable: {error}"

    print("Searching the internet...")

    web_results = search_web(
        question,
        max_results=5
    )

    web_context = "\n\n".join(
        [
            f"""
Title: {result['title']}
URL: {result['url']}
Snippet: {result['snippet']}
"""
            for result in web_results
        ]
    )

    if not web_context:
        web_context = "No web search results were available."

    prompt = f"""
You are an AI research assistant.

Answer the user's research question using the
document research and web search information below.

DOCUMENT RESEARCH:
{document_answer}

WEB SEARCH RESULTS:
{web_context}

USER QUESTION:
{question}

Instructions:
1. Separate findings from uploaded documents and web results.
2. Include URLs when referencing web results.
3. Do not invent facts or citations.
4. Identify conflicting findings.
5. Clearly mention missing evidence.
6. Do not treat search snippets as verified full articles.

Write a structured research summary.
"""

    print("Generating combined research report...")

    final_answer = ask_ollama(prompt)

    return {
        "question": question,
        "document_research": document_answer,
        "web_results": web_results,
        "final_answer": final_answer
    }


if __name__ == "__main__":

    question = input("Enter your research question: ")

    result = conduct_research(question)

    print("\n" + "=" * 60)
    print("RESEARCH REPORT")
    print("=" * 60)

    print(result["final_answer"])
