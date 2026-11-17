
from ddgs import DDGS


def search_web(query, max_results=5):
    """Search the internet and return relevant results."""

    results = []

    try:
        with DDGS() as ddgs:
            search_results = ddgs.text(
                query,
                max_results=max_results
            )

            for result in search_results:
                results.append({
                    "title": result.get("title", ""),
                    "url": result.get("href", ""),
                    "snippet": result.get("body", "")
                })

    except Exception as error:
        print(f"Web search failed: {error}")

    return results


if __name__ == "__main__":

    query = input("Enter your research topic: ")

    results = search_web(query)

    for index, result in enumerate(results, start=1):

        print(f"\nResult {index}")
        print("Title:", result["title"])
        print("URL:", result["url"])
        print("Snippet:", result["snippet"])
