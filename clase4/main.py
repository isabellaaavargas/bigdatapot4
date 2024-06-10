import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json
import glob

import pandas as pd

api_client_id = ""
api_client_secret = ""

# Autenticación con la API de Spotify utilizando las credenciales 

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(api_client_id, api_client_secret))


# Lista de identificadores de las listas de reproducción de Spotify

playlist_list = ["2wWa7oTaziKa9FEKQ12aSs","4zkB78CbXiSLdrs5SzK8yZ","6Xw9RWUaUzw71gESwqIZ8X"]
offset = 0


# Se crea una función para obtener las canciones de una lista de reproducción con un desplazamiento dado

def get_playlist(playlist,offset):
    # Se obtienen los elementos de la lista de reproducción
    resposta = spotify.playlist_items(playlist, offset = offset)
    #Se guarda la respuesta en un archivo JSON

    with open(f'{playlist}-{offset}.json', 'w', encoding='utf-8') as f:
        json.dump(resposta, f, ensure_ascii=False, indent=4)
     
    #Si hay más elementos en la lista de reproducción, se llama recursivamente a la función con un desplazamiento incrementado
    if resposta ["next"] == None:
        print("Final")
        pass
    else:
        offset = offset+100
        print("Nova peticio")
        get_playlist(playlist,offset)


# Se itera sobre las listas de reproducción y llamada a la función get_playlist

for playlist in playlist_list:
    offset = 0
    get_playlist(playlist,offset)


# Obtención de los nombres de todos los archivos JSON en el directorio actual

files= glob.glob("*.json")
list_tracks=[]

# Iteración sobre los archivos JSON para obtener información sobre las canciones

for file in files:
    with open(file) as f:
        d = json.load(f)
        print(d)
        tracks = d["items"]
        # Iteración sobre los elementos de la lista de reproducción para obtener información sobre cada canción
        for track in tracks:
            track_dict ={}
            track_dict["name"] = track["track"]["name"]
            track_dict["popularity"] = track["track"]["popularity"]
            track_dict["artist_name"] = track["track"]["artists"][0]["name"]
            track_dict["duracio_mim"]=round(track["track"]["duration_ms"]/1000/60, 2)
            list_tracks.append(track_dict)


# Creación de un DataFrame de pandas a partir de la lista de canciones

df=pd.DataFrame.from_dict(list_tracks)


# Se guarda el DataFrame en un archivo CSV

df.to_csv("output.csv", index=False, sep=";")
