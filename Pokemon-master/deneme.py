
import requests

url = f'https://pokeapi.co/api/v2/pokemon/6'
response = requests.get(url)
data = response.json()
print(data['sprites']["other"]["home"]["front_default"])