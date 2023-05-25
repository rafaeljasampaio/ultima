import requests

# Nome da moeda que desejamos obter informações
coin = "bitcoin"

# URL da API CoinGecko
url = f"https://api.coingecko.com/api/v3/coins/{coin}"

# Fazendo a solicitação para a API
response = requests.get(url)

if response.status_code == 200:
    # Convertendo a resposta 
    # da API para um dicionário
    data = response.json()
else:
    print("Ocorreu um erro ao obter os dados da API.")


data.keys()
