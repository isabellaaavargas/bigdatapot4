#  (En cuanto al archivo main.py) Análisis de Listas de Reproducción en Spotify

Este script de Python utiliza la API de Spotify para obtener información sobre las canciones de varias listas de reproducción y guardarla en un archivo CSV para su análisis posterior.

## Descripción

El script realiza los siguientes pasos:
1. Se conecta a la API de Spotify utilizando las credenciales proporcionadas.
2. Obtiene las canciones de varias listas de reproducción de Spotify.
3. Guarda la información de las canciones en archivos JSON para cada lista de reproducción.
4. Combina la información de todos los archivos JSON en un solo DataFrame de pandas.
5. Guarda el DataFrame en un archivo CSV para su análisis.

## Resultado

El resultado del script es un archivo CSV llamado `output.csv`, que contiene información sobre las canciones de las listas de reproducción seleccionadas en Spotify.

## Dependencias

El script requiere las siguientes dependencias que deben ser instaladas utilizando pip install:
- `spotipy`: Librería para interactuar con la API de Spotify.
- `pandas`: Librería para manipulación y análisis de datos.

# (En cuanto al archivo twitch) Obtención de Información de Transmisiones en Directo de Twitch

Este script de Python utiliza la API de Twitch para obtener información sobre las transmisiones en directo en español y guarda los resultados en archivos JSON para su análisis posterior.

## Descripción

El script realiza los siguientes pasos:
1. Se inicializa la instancia de la API de Twitch con las claves pública y secreta proporcionadas.
2. Se realiza una llamada a la API de Twitch para obtener información sobre las transmisiones en directo en español.
3. La información obtenida se guarda en archivos JSON, uno por cada página de resultados.
4. Se maneja la paginación de los resultados para obtener todas las transmisiones disponibles.
5. Se incluye un control de velocidad para evitar exceder los límites de la API de Twitch.

## Resultado

El resultado del script es una serie de archivos JSON que contienen información detallada sobre las transmisiones en directo de Twitch en español.

## Dependencias

El script requiere las siguientes dependencias que deben ser instaladas con pip install:
- `twitchAPI`: Librería para interactuar con la API de Twitch.
- `json`: Librería estándar de Python para manipulación de archivos JSON.
- `time`: Librería estándar de Python para manejo de tiempos.

