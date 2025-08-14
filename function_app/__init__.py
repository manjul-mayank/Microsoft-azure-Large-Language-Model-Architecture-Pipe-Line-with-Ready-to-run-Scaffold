# -------- 7) Azure Functions (HTTP Trigger) --------
import json
import azure.functions as func
import asyncio
from services.retriever import hybrid_search, format_context
from services.llm import chat_complete
from api.integrations import fetch_dummy_info

SYSTEM_PROMPT = """You are an enterprise assistant. Cite sources when available.
Use the CONTEXT and any API INFO to answer succinctly.
"""

async def run_chain(question: str) -> str:
    docs = hybrid_search(question, k=4)          # (#4)
    context = format_context(docs)
    api_info = await fetch_dummy_info(question)  # (#5)
    user_prompt = f"Question: {question}\n\nAPI INFO: {api_info}\n\nCONTEXT:\n{context}"
    answer = chat_complete(SYSTEM_PROMPT, user_prompt)  # (#3)
    return answer

async def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        body = req.get_json()
    except ValueError:
        return func.HttpResponse("Invalid JSON", status_code=400)

    question = (body.get("question") or "").strip()
    if not question:
        return func.HttpResponse("Field 'question' is required", status_code=400)

    answer = await run_chain(question)
    return func.HttpResponse(
        json.dumps({"answer": answer}),
        mimetype="application/json",
        status_code=200
    )
