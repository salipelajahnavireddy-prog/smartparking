import requests


url = "http://127.0.0.1:8000/update/"


data = {
    "slot1": "occupied",
    "slot2": "available",
    "slot3": "occupied"
}


response = requests.post(
    url,
    json=data
)


print(response.text)