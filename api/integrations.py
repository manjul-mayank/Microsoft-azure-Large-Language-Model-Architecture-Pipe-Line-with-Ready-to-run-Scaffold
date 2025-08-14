# -------- 5) APIs (External/Internal Integrations) --------
# Example: a stub that would call an external API (e.g., CRM, weather, ERP).
# Replace with real calls and auth as needed.
import httpx

async def fetch_dummy_info(topic: str) -> str:
    # Demo stub to keep this offline-friendly.
    # Example for real use:
    # async with httpx.AsyncClient(timeout=10) as client:
    #     r = await client.get('https://api.example.com/data', params={'q': topic})
    #     r.raise_for_status()
    #     data = r.json()
    #     return data.get('summary', 'No data')
    return f"No external API configured. (topic={topic})"
