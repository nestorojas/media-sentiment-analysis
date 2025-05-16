import os
import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("NEWSDATA_API_KEY")

url = "https://newsdata.io/api/1/news"
params = {
    "apikey": api_key,
    "country": "us",
    "language": "en",
    "category": "business"
}

response = requests.get(url, params=params)
data = response.json()
print(data)