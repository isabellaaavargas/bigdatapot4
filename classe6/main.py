### Librerías a instal·lar #################
# pip install beautifulsoup4 #
# pip install request #
# pip install spotipy #
# pip install lxml #
# pip install beautifulsoup4 #
# pip install openpyxl #
#############################################

import requests
from bs4 import BeautifulSoup #beautifulsoup procesa el codigo
import pandas as pd
import time
import glob
import spotipy
import json
from spotipy.oauth2 import SpotifyClientCredentials

SPOTIPY_CLIENT_ID = ""
SPOTIPY_CLIENT_SECRET = ""

auth_manager = SpotifyClientCredentials(SPOTIPY_CLIENT_ID,  SPOTIPY_CLIENT_SECRET)
sp  =  spotipy.Spotify(auth_manager=auth_manager)

rango = range(2000,2024,1)
for r in rango:
    print(r)

def extract_wiki(rango):
    for r in rango:
        try:
            resposta = requests.get (f"https://es.wikipedia.org/wiki/Festival_de_la_Canci%C3%B3n_de_Eurovisi%C3%B3n_{r}")
            codi_web = (resposta.text) #aqui tenemos el código de la página web

            soup = BeautifulSoup(codi_web, 'html.parser')
            final = soup.find('span', id="Final")  #para buscar el h3 que hace referencia a la palabra final de la pagina web
            tabla = final.find_next("table")  # Buscamos la tabla después del elemento <span>
            df = pd.read_html(str(tabla))[0]

            print(df)
            df.to_excel(f"final-{r}.xlsx",index=False)
            print(f"todo bien en {r}")
            time.sleep(1)
        except AttributeError:
            print(f"problema en {r}")

# extract_wiki(rango) se comenta la funcion porque ya no se hace scrapping
def juntar ():
    files = glob.glob("*.xlsx")
    print(files)

    llista_dfs=[]
    for f in files:
        df = pd.read_excel(f)
        any = f.split("-")[1].split(".")[0]
        df["año"] = any
        df.columns.values[2] = "cantante"
        df.columns.values[5] = "puntos"
        df.columns.values[0] = "N."

        llista_dfs.append(df)

    final_df = pd.concat(llista_dfs)
    final_df.to_excel("final-final.xlsx",index=False)
    print(final_df)

#juntar()
df=pd.read_excel("final-final.xlsx")
print (df)

for index,row in df.iterrows():
    cantant = row["cantante"]
    song = row["Canción"]
    año = row["año"]
    q=f"{song} {cantant} Eurovision"
    print(q)
    resposta = sp.search(q, limit=10, offset=0, type='track', market=None)
    resposta["query"] = q

    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(resposta, f, ensure_ascii=False, indent=4)
    print("Fet!")
    time.sleep(15)
