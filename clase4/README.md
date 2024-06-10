# Análisis de Listas de Reproducción en Spotify

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
