import urllib.request
import json

#função que faz a comunicação com a api viacep e retorna o endereço do cep informado
def cep(cep_informado):
    """"faz a comunicação com a api viacep e retorna o endereço do cep informado"""

    try:
        with urllib.request.urlopen(f"https://viacep.com.br/ws/{cep_informado}/json/") as url:
            data = json.loads(url.read().decode('utf-8'))
            return data
    except Exception as error:
        print(f"Erro ao buscar CEP.{error}")
        return None

#função que traz a cotação do dolar do dia
def cotacao():
    """traz a dolar do dia"""
    try:
        with urllib.request.urlopen("https://economia.awesomeapi.com.br/json/last/USD-BRL") as url:
            data = json.loads(url.read().decode('utf-8'))
            return float(data['USDBRL']['bid'])
    except Exception as error:
        print(f"Erro ao buscar cotação.{error}")
        return 6

print(cotacao())
