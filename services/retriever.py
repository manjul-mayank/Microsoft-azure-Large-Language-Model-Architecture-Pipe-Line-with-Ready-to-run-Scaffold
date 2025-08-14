import os
from typing import List, Dict, Any
from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient

# -------- 4) Azure AI Search (Vector/Hybrid Retrieval) --------
def get_search_client() -> SearchClient:
    endpoint = os.getenv("AZURE_SEARCH_ENDPOINT")
    key = os.getenv("AZURE_SEARCH_KEY")
    index_name = os.getenv("AZURE_SEARCH_INDEX")
    if not all([endpoint, key, index_name]):
        raise RuntimeError("Missing one of AZURE_SEARCH_ENDPOINT, AZURE_SEARCH_KEY, AZURE_SEARCH_INDEX")
    return SearchClient(endpoint=endpoint, index_name=index_name, credential=AzureKeyCredential(key))

def hybrid_search(query: str, k: int = 5) -> List[Dict[str, Any]]:
    client = get_search_client()
    # For portability: simple keyword search. If vector/semantic is enabled, you can expand here.
    results = client.search(search_text=query, top=k)
    hits = []
    for r in results:
        hits.append({
            "content": r.get("content", ""),
            "source": r.get("source", r.get("id", ""))
        })
    return hits

def format_context(docs: List[Dict[str, Any]]) -> str:
    blocks = []
    for d in docs:
        src = d.get("source", "")
        txt = d.get("content", "")
        blocks.append(f"Source: {src}\n{txt}")
    return "\n\n".join(blocks)
