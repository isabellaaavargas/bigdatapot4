import spotipy  # libreria de spotify que ha sido creada por alguien
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd


#Credenciales de mi API de Spotify

api_client_id = ""  # desde mi dashboard de spotify
api_client_secret = ""


#Para hacer la autenticación con la API de Spotify utilizando las credenciales proporcionadas

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(api_client_id, api_client_secret))


# ID del artista inicial (Rosalía en este caso)

artist_id = "7ltDVBr6mKbRvohxheJ9h1"  # la ultima parte del link del artista spotify web player

llista_artistes = []


#Definición de una función para obtener artistas relacionados

def get_related(artist_id):
    resposta = spotify.artist_related_artists(artist_id)
    return resposta


#Se llama a la función para obtener artistas relacionados con el artista inicial

result = get_related(artist_id)


#Inicialización de una lista para almacenar los artistas relacionados

llista_de_relacionats=[]


# Se itera sobre los artistas relacionados obtenidos

for artist in result["artists"]: #para iterar en la resposta ("artists" viene del json)
    artista = {}
    artista["origen"] = "rosalia"
    artista["desti"]=artist["name"]
    artista["generes"] = artist["genres"]
    artista["id"]=artist["id"]
    llista_de_relacionats.append(artista)


# Se inicializa una lista definitiva para almacenar todos los artistas relacionados de segundo nivel

llista_definitiva=[]


# Se añaden los artistas relacionados de primer nivel a la lista definitiva y se obtienen sus artistas relacionados

for a in llista_de_relacionats:
    llista_definitiva.append(a)
    id=a["id"]
    result = get_related(id)

    
    # Iteración sobre los artistas relacionados de segundo nivel

    for artist in result["artists"]:  # para iterar en la resposta
        artista = {}
        artista["origen"] = a["desti"]
        artista["desti"] = artist["name"]
        artista["generes"] = artist["genres"]
        artista["id"] = artist["id"]
        llista_definitiva.append(artista)


# Inicialización de una lista para almacenar las tuplas de relaciones entre artistas

llista_tuples=[]


# Se crean tuplas de relaciones entre artistas de primer y segundo nivel

for i in llista_definitiva:
    source= i["origen"]
    target= i["desti"]
    tupla= (source,target)
    llista_tuples.append(tupla)


# Por otro lado se crean tuplas de relaciones entre artistas y sus géneros

for i in llista_definitiva:
    for g in i["generes"]:
        source =i ["origen"]
        target = g
        tupla = (source,target)
        llista_tuples.append(tupla)


# Se crea el DataFrame de pandas a partir de las tuplas de relaciones

df= pd.DataFrame(llista_tuples, columns =["source","target"])
print(df)

# Se guarda el DataFrame en un archivo CSV

df.to_csv("graf.generes.csv",sep=",",index=False)

