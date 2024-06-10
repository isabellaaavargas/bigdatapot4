### Librerías a instal·lar #################
# pip install beautifulsoup4 #
# pip install request #
# pip install spotipy #
# pip install lxml #
# pip install beautifulsoup4 #
# pip install openpyxl #
#############################################


#Importación de las librerías

import requests # Para realizar solicitudes HTTP
from bs4 import BeautifulSoup #beautifulsoup procesa el codigo HTML de la página
import pandas as pd # Para manipular datos como DataFrames
import time  # Para introducir pausas en el código
import glob  # Para buscar archivos en un directorio
import spotipy  # Para interactuar con la API de Spotify
import json   # Para manejar datos en formato JSON
from spotipy.oauth2 import SpotifyClientCredentials  # Para autenticarse en la API de Spotify


# Definición de mis credenciales de Spotify

SPOTIPY_CLIENT_ID = ""
SPOTIPY_CLIENT_SECRET = ""


# Rango de años para web scraping en Wikipedia

auth_manager = SpotifyClientCredentials(SPOTIPY_CLIENT_ID,  SPOTIPY_CLIENT_SECRET)
sp  =  spotipy.Spotify(auth_manager=auth_manager)


# Función para extraer datos de Wikipedia (actualmente comentada)

rango = range(2000,2024,1)
for r in rango:
    print(r)

def extract_wiki(rango):
    for r in rango:
        try:
            # Para obtener el contenido de la página web
            resposta = requests.get (f"https://es.wikipedia.org/wiki/Festival_de_la_Canci%C3%B3n_de_Eurovisi%C3%B3n_{r}")
            codi_web = (resposta.text) #aqui tenemos el código de la página web
            # Parsear el código HTML con BeautifulSoup
            soup = BeautifulSoup(codi_web, 'html.parser')
            final = soup.find('span', id="Final")  #para buscar el h3 que hace referencia a la palabra final de la pagina web
            tabla = final.find_next("table")  # Buscamos la tabla después del elemento <span>
            df = pd.read_html(str(tabla))[0] # Convierte la tabla HTML a DataFrame
            
            
            # Imprime y guarda el DataFrame en un archivo Excel
            print(df)
            df.to_excel(f"final-{r}.xlsx",index=False)
            print(f"todo bien en {r}")
            time.sleep(1) # Se introduce una pausa de 1 segundo para evitar que colapse
        except AttributeError:
            print(f"problema en {r}")

# Función para combinar archivos Excel (actualmente comentada)
def juntar ():
    files = glob.glob("*.xlsx") # Busca archivos Excel en el directorio actual
    print(files)

    llista_dfs=[]
    for f in files:
        df = pd.read_excel(f) # Lee cada archivo Excel
        any = f.split("-")[1].split(".")[0] # Extrae el año del nombre del archivo
        df["año"] = any # Agrega una columna "año" al DataFrame
        df.columns.values[2] = "cantante" # Renombra la tercera columna como "cantante"
        df.columns.values[5] = "puntos"  # Renombra la sexta columna como "puntos"
        df.columns.values[0] = "N." # Renombra la primera columna como "N."
        # Agrega el DataFrame a una lista
        llista_dfs.append(df)
   
    # Concatena todos los DataFrames en uno solo
    final_df = pd.concat(llista_dfs)
    
    # Se guarda el DataFrame combinado en un archivo Excel
    final_df.to_excel("final-final.xlsx",index=False)
    print(final_df)

# Función para buscar canciones en Spotify
# Se comenta porque ya no se hace scraping
# extract_wiki(rango)

# Lee el archivo Excel que contiene los datos combinados de Eurovisión
df=pd.read_excel("final-final.xlsx")
print (df)

# Bucle para buscar canciones en Spotify para cada fila del DataFrame

for index,row in df.iterrows():
    cantant = row["cantante"] # Obtiene el nombre del cantante
    song = row["Canción"] # Obtiene el nombre de la canción
    año = row["año"] # Obtiene el año
    q=f"{song} {cantant} Eurovision" # Crea una consulta de búsqueda
    print(q)

    # Realiza la búsqueda en Spotify y guarda la respuesta en un archivo JSON
    resposta = sp.search(q, limit=10, offset=0, type='track', market=None)
    resposta["query"] = q

    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(resposta, f, ensure_ascii=False, indent=4)
    print("Fet!")
    time.sleep(15)  # Se introduce una pausa de 15 segundos entre cada búsqueda
