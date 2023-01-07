import requests
import time

data = []

while True:
    while len(data)==0:
        data = []
        time.sleep(5)
        try:
            response = requests.get('http://127.0.0.1:5000/data?id=2')
            data = response.json()["data"]
        except requests.exceptions.RequestException:
            pass
    print(response.json())
