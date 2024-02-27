import spotipy  # libreria de spotify que ha sido creada por alguien
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd

api_client_id = ""  # desde mi dashboard de spotify
api_client_secret = ""

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(api_client_id, api_client_secret))

artist_id = "7ltDVBr6mKbRvohxheJ9h1"  # la ultima parte del link del artista spotify web player

llista_artistes = []
def get_related(artist_id):
    resposta = spotify.artist_related_artists(artist_id)
    return resposta

result = get_related(artist_id)

llista_de_relacionats=[]
for artist in result["artists"]: #para iterar en la resposta ("artists" viene del json)
    artista = {}
    artista["origen"] = "rosalia"
    artista["desti"]=artist["name"]
    artista["generes"] = artist["genres"]
    artista["id"]=artist["id"]
    llista_de_relacionats.append(artista)

llista_definitiva=[]
for a in llista_de_relacionats:
    llista_definitiva.append(a)
    id=a["id"]
    result = get_related(id)

    for artist in result["artists"]:  # para iterar en la resposta
        artista = {}
        artista["origen"] = a["desti"]
        artista["desti"] = artist["name"]
        artista["generes"] = artist["genres"]
        artista["id"] = artist["id"]
        llista_definitiva.append(artista)

llista_tuples=[]
for i in llista_definitiva:
    source= i["origen"]
    target= i["desti"]
    tupla= (source,target)
    llista_tuples.append(tupla)

for i in llista_definitiva:
    for g in i["generes"]:
        source =i ["origen"]
        target = g
        tupla = (source,target)
        llista_tuples.append(tupla)

df= pd.DataFrame(llista_tuples, columns =["source","target"])
print(df)
df.to_csv("graf.generes.csv",sep=",",index=False)

