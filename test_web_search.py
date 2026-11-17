
from web_search import search_web


def test_web_search():

    results = search_web(
        "Latest developments in retrieval augmented generation",
        max_results=3
    )

    assert isinstance(results, list)

    if results:
        assert "title" in results[0]
        assert "url" in results[0]
        assert "snippet" in results[0]

        print("Web search successful!")
        print("Results found:", len(results))
    else:
        print("No results returned. Check network availability.")
