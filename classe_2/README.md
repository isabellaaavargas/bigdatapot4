# Spotify Related Artists Data Extractor

Este repositorio contiene un script en Python (main.py) que se conecta a mi API de Spotify para obtener una lista de artistas relacionados con un artista específico (en este caso, Rosalía) y guarda la información de esos artistas en un archivo Excel.

## Descripción

El script realiza los siguientes pasos:
1. Se conecta a la API de Spotify utilizando mis credenciales proporcionadas.
2. Obtiene una lista de artistas relacionados con el artista especificado (Rosalía).
3. Guarda la respuesta de la API en un archivo JSON.
4. Extrae y estructura la información relevante de cada artista, como nombre, seguidores, link de Spotify y ID.
5. Almacena los datos en un archivo Excel llamado `dataset.xlsx`.

## Resultado

El script genera un archivo Excel (`dataset.xlsx`) que contiene la siguiente información para cada artista relacionado con el artista especificado:
- Nombre del artista
- ID del artista
- Número de seguidores
- Enlace al perfil de Spotify del artista
- ID del artista semilla (Rosalía)

## Dependencias

Las siguientes dependencias son necesarias para ejecutar el script:
- `spotipy`: Librería para interactuar con la API de Spotify.
- `pandas`: Librería para manipulación y análisis de datos, utilizada para crear el archivo Excel.

Estas dependencias fueron instalads utilizando pip install
