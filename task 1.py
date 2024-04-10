import requests
import time

url = "https://jsonplaceholder.typicode.com/posts/"

def load_urls(url):
    response = requests.get(url)
    return response.json()
