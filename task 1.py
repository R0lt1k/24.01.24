import requests
import time

def load_urls(url):
    response = requests.get(url)
    return response.json()
