import requests

url = "http://localhost:8000/api/vidas"
headers = {
        'Content-Type': 'application/json',
    }

# Envia os dados extraídos da planilha para a API
def Sender(vida): 
    response = requests.post(url, json=vida, headers=headers)
    vida_registrada = response.json()
    print(f"STATUS - {response.status_code}")
    print(vida_registrada)
    print(50*"__")
