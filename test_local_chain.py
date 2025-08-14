# -------- 1) Python (Local Runner) --------
# Orchestrates: query -> retrieve (#4) -> optional API (#5) -> call LLM (#3)

import sys
import asyncio
from services.retriever import hybrid_search, format_context
from services.llm import chat_complete
from api.integrations import fetch_dummy_info

SYSTEM_PROMPT = """You are an enterprise assistant. Cite sources when available.
Use the CONTEXT and any API INFO to answer succinctly.
"""

async def main():
    question = " ".join(sys.argv[1:]) or "What does our refund policy say?"
    docs = hybrid_search(question, k=4)
    context = format_context(docs)
    api_info = await fetch_dummy_info(question)
    user_prompt = f"Question: {question}\n\nAPI INFO: {api_info}\n\nCONTEXT:\n{context}"
    answer = chat_complete(SYSTEM_PROMPT, user_prompt)
    print("ANSWER:\n", answer)

if __name__ == "__main__":
    asyncio.run(main())
