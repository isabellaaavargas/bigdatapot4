# Análisis de Relaciones entre Artistas y Géneros en Spotify

Este script de Python utiliza mi API de Spotify para obtener información sobre artistas relacionados y sus géneros musicales. Luego, crea un grafo que muestra las relaciones entre artistas y géneros en formato de archivo CSV.

## Descripción

El script realiza los siguientes pasos:
1. Se conecta a la API de Spotify utilizando las credenciales proporcionadas.
2. Obtiene los artistas relacionados de un artista inicial (en este caso, Rosalía).
3. Para cada artista relacionado, obtiene información sobre sus géneros musicales.
4. Crea un grafo que muestra las relaciones entre artistas y géneros.
5. Guarda el grafo en formato CSV para su posterior análisis.

## Resultado

El resultado del script es un archivo CSV llamado `graf.generes.csv`. Este archivo contiene las relaciones entre artistas y géneros musicales, lo que permite analizar la distribución de géneros entre los artistas relacionados.

## Dependencias

El script requiere las siguientes dependencias que deben ser instaladas:
- `spotipy`: Librería para interactuar con la API de Spotify.
- `pandas`: Librería para manipulación y análisis de datos.
- `openpyxl`: Librería para trabajar con archivos Excel (.xlsx).

Se pueden instalar las librerías utilizando pip:

```sh
pip install json
