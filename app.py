import requests

API = "SUA API"
URL = "https://newsapi.org/v2/everything"
noticia = input('o que você quer: ')
params = {
    "q": noticia,  # Palavra-chave
    "language": "pt",  # Idioma português
    "sortBy": "publishedAt",  # Ordenar por data de publicação
    "apiKey": API
}
response = requests.get(URL, params=params)
data = response.json()

if data["status"] == "ok":
    print(f" Total de Resultados: {data['totalResults']}")
    for article in data["articles"]:
        print(f"Nome:{article['source']['name']} \n titulo: {article['title']}")
        print(f'{article['publishedAt']}')
#       print(f"{article['title']} - {article['source']['name']}")
