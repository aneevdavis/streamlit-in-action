import requests

API_URL = "https://api.api-ninjas.com/v1/quotes"
QUOTE_CATEGORY = "inspirational"

def generate_quote(api_key):
    params = {"category": QUOTE_CATEGORY}
    headers = {"X-Api-Key": api_key}
    response = requests.get(API_URL, params=params, headers=headers)
    quote_obj = response.json()[0]
    if response.status_code == requests.codes.ok:
        return f"{quote_obj['quote']} -- {quote_obj['author']}"
    return f"Just do it! -- Shia LaBeouf"
