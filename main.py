import spotipy  #libreria de spotify que ha sido creada por alguien
from spotipy.oauth2 import SpotifyClientCredentials
import json
#llamando a la libreria pandas para que se convierta en excel
import pandas as pd

api_client_id = "" #desde mi dashboard de spotify
api_client_secret = ""

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(api_client_id,api_client_secret))

artist_inicial = "7ltDVBr6mKbRvohxheJ9h1" #la ultima parte del link del artista spotify web player
resposta = spotify.artist_related_artists(artist_inicial)

with open('data_2json', 'w', encoding='utf-8') as f:
    json.dump(resposta, f, indent=4)

artistes = resposta["artists"] #para acceder a la lista de artistas del data 2 json

llista_artistes = []

for a in artistes:
    name = a["name"] #para entrar a cada nombre de la lista de artistas del data 2 json
    seguidores = a["followers"]["total"] #para entrar a la lista de seguidores de cada artista y se ha de nombrar tambien el total
    link = a["external_urls"]["spotify"] #para que enseñe el link de cada artista
    id = a["id"] #se añade el id de todos los artistas relacionados de la rosalia

    # para crear el data set de pandas
    frame = pd.DataFrame({
        "semilla": artist_inicial,
        "name": name,
        "id": id,
        "seguidores": seguidores,
        "link": link,
    }, index=[0])
    llista_artistes.append(frame)

final = pd.concat(llista_artistes)
print(final)
final.to_excel("dataset.xlsx")
print("TERMINADO")


