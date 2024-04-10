import requests
import time

url = "https://jsonplaceholder.typicode.com/posts/"

def load_urls(url, file_name):
    response = requests.get(url)
    with open(file_name, "w") as file:
        file.write(response.text)

start = time.time()
for i in range(1, 10):
    load_urls(url, f"post{i}.json")
end = time.time()
print("Время выполнения: ", end - start)
