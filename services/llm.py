import os
from openai import AzureOpenAI

# -------- 3) Azure OpenAI (LLM) --------
def get_azure_openai_client():
    endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
    key = os.getenv("AZURE_OPENAI_KEY")
    api_version = os.getenv("AZURE_OPENAI_API_VERSION", "2024-05-01-preview")
    if not endpoint or not key:
        raise RuntimeError("Missing AZURE_OPENAI_ENDPOINT or AZURE_OPENAI_KEY")
    return AzureOpenAI(azure_endpoint=endpoint, api_key=key, api_version=api_version)

def chat_complete(system_prompt: str, user_prompt: str) -> str:
    client = get_azure_openai_client()
    model = os.getenv("AZURE_OPENAI_DEPLOYMENT")  # deployed model name
    if not model:
        raise RuntimeError("Missing AZURE_OPENAI_DEPLOYMENT")
    resp = client.chat.completions.create(
        model=model,
        messages=[
            { "role": "system", "content": system_prompt },
            { "role": "user", "content": user_prompt }
        ],
        temperature=0.2,
        max_tokens=800
    )
    return resp.choices[0].message.content.strip()
