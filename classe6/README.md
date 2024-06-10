# Análisis de Datos de Eurovisión y Búsqueda de Canciones en Spotify

Este script de Python realiza análisis de datos del Festival de Eurovisión utilizando web scraping en Wikipedia para obtener datos históricos sobre los finalistas y sus puntuaciones. Luego, busca canciones relacionadas en Spotify utilizando la API de Spotify.

## Descripción

El código realiza las siguientes acciones:

1. **Web Scraping en Wikipedia**: Extrae datos del Festival de Eurovisión de diferentes años, como los finalistas y sus puntuaciones, utilizando web scraping en Wikipedia.
2. **Manipulación de Datos con Pandas**: Utiliza la librería pandas para manipular los datos extraídos y combinarlos en un único DataFrame.
3. **Búsqueda de Canciones en Spotify**: Utiliza la API de Spotify para buscar canciones relacionadas con los finalistas del Festival de Eurovisión de cada año.
4. **Guardado de Resultados**: Guarda los resultados de la búsqueda en un archivo JSON y realiza una pausa entre cada búsqueda para evitar exceder los límites de la API de Spotify.

## Dependencias

El script utiliza las siguientes librerías de Python:

- `requests`: Para realizar solicitudes HTTP y obtener el contenido de las páginas web.
- `beautifulsoup4`: Para parsear el HTML de las páginas web y extraer los datos deseados.
- `pandas`: Para manipular los datos como DataFrames.
- `spotipy`: Para interactuar con la API de Spotify y realizar búsquedas de canciones.

Hay que asegurarse de tener estas librerías instaladas antes de ejecutar el script.

