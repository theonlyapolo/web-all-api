import requests
import json

nomepoke = input('Digite um nome de pokémon: ')
url = f'https://pokeapi.co/api/v2/pokemon/{nomepoke}'
retorno = requests.get(url)
retorno = json.loads(retorno.text)

print(retorno['abilities'])