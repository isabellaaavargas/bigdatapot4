#Importaciones de librerias necesarias

import spotipy  #libreria de spotify que ha sido creada por alguien
from spotipy.oauth2 import SpotifyClientCredentials
import json #llamando a la libreria pandas para que se convierta en excel
import pandas as pd


#Aquí defino las credenciales de la API de spotify

api_client_id = "" #desde mi dashboard de spotify
api_client_secret = ""


#Autenticación con la API de Spotify utilizando las credenciales

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(api_client_id,api_client_secret))


#Especificación del artista inicial (Rosalía en este caso)

artist_inicial = "7ltDVBr6mKbRvohxheJ9h1" #Se ha de coger la última parte del link del artista spotify web player


#Para obtener artistas relacionados con el artista inicial

resposta = spotify.artist_related_artists(artist_inicial)


#Guardo la respuesta de la API en un archivo JSON

with open('data_2json', 'w', encoding='utf-8') as f:
    json.dump(resposta, f, indent=4)


#Para acceder a la lista de artistas relacionados desde la respuesta JSON

artistes = resposta["artists"] #para acceder a la lista de artistas del data 2 json


#Inicializo una lista para almacenar los datos de los artistas

llista_artistes = []


#Recorrido por cada artista en la lista de artistas relacionados y extracción de la información relevante

for a in artistes:
    name = a["name"] #para entrar a cada nombre de la lista de artistas del data 2 json
    seguidores = a["followers"]["total"] #para entrar a la lista de seguidores de cada artista y se ha de nombrar tambien el total
    link = a["external_urls"]["spotify"] #para que enseñe el link de cada artista
    id = a["id"] #se añade el id de todos los artistas relacionados de la rosalia

    #Para crear el data set de pandas para cada artista con la información extraída
    frame = pd.DataFrame({
        "semilla": artist_inicial,
        "name": name,
        "id": id,
        "seguidores": seguidores,
        "link": link,
    }, index=[0])
    #Adición de cada DataFrame a la lista de artistas
    llista_artistes.append(frame)


#Concatenación de todos los DataFrames en uno solo

final = pd.concat(llista_artistes)
print(final)


#Guardo el dataset en un archivo excel

final.to_excel("dataset.xlsx")
print("TERMINADO")
