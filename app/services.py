import requests
import unidecode

def consulta_api(cidade, key):
    cidade = unidecode.unidecode(cidade)
    cidade = cidade.replace(' ', '%20')
    retorno = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={key}')
    if retorno.status_code == 200:
        tempo_cidade = retorno.json()
        return tempo_cidade
    else:
        return
