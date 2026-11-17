
from pdf_processor import extract_text_from_pdf


def test_pdf_extraction():
    pages = extract_text_from_pdf(
        "documents/research_paper.pdf"
    )

    assert len(pages) > 0
    assert "text" in pages[0]
    assert pages[0]["text"].strip()

    print("PDF extraction successful!")
    print("Pages extracted:", len(pages))
