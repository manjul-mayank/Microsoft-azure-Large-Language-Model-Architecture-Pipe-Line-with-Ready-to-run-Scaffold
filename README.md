
# 🚀 Azure LLM Pipeline Scaffold: RAG + OpenAI + Serverless

**Deploy a production-ready LLM pipeline on Azure in minutes!**  
✨ *Retrieval-Augmented Generation (RAG), Azure OpenAI, AI Search, and Functions—fully integrated.*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org)
[![Azure Ready](https://img.shields.io/badge/Azure-Ready-0089D6)](https://azure.microsoft.com)
![GitHub stars](https://img.shields.io/github/stars/your-repo?style=social)

## 📊 Architecture Flow
![Azure LLM Pipeline Architecture](azure_llm_arch_flow_full%20chart.png)
*Example: Querying a refund policy with AI-powered retrieval.*

---

## 🔥 Features
- **End-to-End RAG Pipeline**: From documents to AI answers.
- **Serverless Deployment**: Scalable via Azure Functions.
- **Hybrid Search**: Vector + keyword retrieval with Azure AI Search.
- **Plug & Play**: Add your data, tweak prompts, deploy.

---

# Azure LLM App — Architecture Flow (1→7)

This scaffold demonstrates the end-to-end flow:

1) **Python (Backend code)**
2) **Azure (Cloud platform)**
3) **Azure OpenAI (LLM)**
4) **Azure AI Search (vector/hybrid retrieval)**
5) **APIs (external/internal integrations)**
6) **LangChain (optional orchestration)**
7) **Azure Functions (serverless deployment)**

> Plug in your credentials and an Azure AI Search index (`content`, `contentVector` fields suggested).

## Quick Start (Local)

```bash
pip install -r requirements.txt

export AZURE_OPENAI_ENDPOINT="https://<your-aoai>.openai.azure.com"
export AZURE_OPENAI_KEY="<your-aoai-key>"
export AZURE_OPENAI_DEPLOYMENT="<your-deployment-name>"   # e.g., gpt-4o, gpt-35-turbo
export AZURE_OPENAI_API_VERSION="2024-05-01-preview"

export AZURE_SEARCH_ENDPOINT="https://<your-search>.search.windows.net"
export AZURE_SEARCH_KEY="<your-search-admin-key>"
export AZURE_SEARCH_INDEX="<your-index-name>"

python test_local_chain.py "What does our refund policy say?"
```

## Run as Azure Function (HTTP Trigger)

```bash
# Install Azure Functions Core Tools first
func start

# In another terminal
curl -X POST http://localhost:7071/api/chat   -H "Content-Type: application/json"   -d '{"question":"Summarize our refund policy"}'
```

## Files (mapped 1→7)
- `test_local_chain.py` — **(1)** Orchestrates retrieval → API → LLM locally
- `host.json` — **(2)** Azure app host settings
- `requirements.txt` — deps for local and Functions
- `services/llm.py` — **(3)** Azure OpenAI wrapper
- `services/retriever.py` — **(4)** Azure AI Search retrieval
- `api/integrations.py` — **(5)** API integration stub
- `services/langchain_chain.py` — **(6)** Optional LangChain mini-chain
- `function_app/__init__.py` — **(7)** Azure Functions HTTP trigger
- `function_app/function.json` — bindings

## Minimal Index Schema Expectation
- `id`: Edm.String (key)
- `content`: Edm.String
- `contentVector`: Collection(Edm.Single)  # vector field (e.g., 1536 dims)
- `source`: Edm.String (optional)

## Security Notes
- Use Key Vault or environment variables for secrets.
- Validate and size-limit user inputs.
- Consider content filters and network restrictions for Functions.
