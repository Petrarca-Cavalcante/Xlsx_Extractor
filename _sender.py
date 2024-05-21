import requests

url = "http://localhost:8000/api/vidas"
headers = {
        'Content-Type': 'application/json',
    }

def Sender(vida): 
    print(vida, 10*"-")
    response = requests.post(url, json=vida, headers=headers)
    print(response.content)
