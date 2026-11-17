
from rag import answer_from_documents


def test_rag_answer():

    answer = answer_from_documents(
        "What is the main contribution of this research paper?"
    )

    assert isinstance(answer, str)
    assert len(answer.strip()) > 0

    print("RAG answer generated successfully!")
    print(answer)
