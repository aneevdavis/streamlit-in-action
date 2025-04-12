import requests

API_URL = "https://api.api-ninjas.com/v1/dadjokes"

def generate_joke(api_key):
    headers = {"X-Api-Key": api_key}
    response = requests.get(API_URL, headers=headers)
    if response.status_code == requests.codes.ok:
        joke_obj = response.json()[0]
        return joke_obj['joke']
    # Fall back to a default joke if the API fails
    return f"Time flies like an arrow. Fruit flies like a banana."
