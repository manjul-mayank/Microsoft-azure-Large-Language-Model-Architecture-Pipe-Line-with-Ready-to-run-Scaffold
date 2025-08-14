# -------- 6) LangChain (Optional Orchestration) --------
from typing import Callable
from langchain_openai import AzureChatOpenAI
from langchain.prompts import ChatPromptTemplate

SYSTEM_TEMPLATE = """You are a helpful assistant. Use the provided CONTEXT to answer.
If the answer is not in the context, say you don't know. Be concise.
CONTEXT:
{context}
"""

def build_chain() -> Callable[[str, str], str]:
    llm = AzureChatOpenAI(temperature=0.2)  # reads Azure env vars
    prompt = ChatPromptTemplate.from_messages([
        ("system", SYSTEM_TEMPLATE),
        ("human", "{question}")
    ])

    def run(context: str, question: str) -> str:
        msg = prompt.format(context=context, question=question)
        resp = llm.invoke(msg.to_messages())
        return resp.content.strip()

    return run
