import pandas as pd
from googleapiclient.discovery import build
from datetime import datetime

# Hemos insertado nuestra clave de API aquí
API_KEY = 'AIzaSyDMKSNAoeVyq4NPWup1t1TVYqSkBT5-5GI'

def buscar_videos(query, max_results=None):
    # Aquí construimos el cliente de la API de YouTube
    youtube = build('youtube', 'v3', developerKey=API_KEY)

    # Inicializamos una lista para almacenar la información de los videos
    videos = []
    next_page_token = None
    total_results = 0

    while True:
        # Creamos una solicitud a la API de YouTube para buscar videos que coincidan con la consulta
        request = youtube.search().list(
            q=query,
            part='id,snippet',
            type='video',
            maxResults=min(50, max_results - total_results if max_results else 50),
            pageToken=next_page_token
        )

        # Ejecutamos la solicitud y almacenamos la respuesta
        response = request.execute()

        for item in response['items']:
            # Extraemos el ID, título y descripción del video
            video_id = item['id']['videoId']
            video_title = item['snippet']['title']
            video_description = item['snippet']['description']

            # Realizamos otra solicitud para obtener las estadísticas del video
            stats_request = youtube.videos().list(
                part='statistics,snippet',
                id=video_id
            )
            stats_response = stats_request.execute()

            # Obtenemos las estadísticas y el snippet del video
            video_stats = stats_response['items'][0]['statistics']
            video_snippet = stats_response['items'][0]['snippet']

            # Extraemos variables adicionales como vistas, likes, canal y fecha de publicación
            views = video_stats.get('viewCount', 'No disponible')
            likes = video_stats.get('likeCount', 'No disponible')
            channel_title = video_snippet.get('channelTitle', 'No disponible')
            published_at = video_snippet.get('publishedAt', 'No disponible')

            # Formateamos la fecha de publicación
            published_at = datetime.strptime(published_at, '%Y-%m-%dT%H:%M:%SZ')

            # Construimos el enlace del video
            video_link = f'https://www.youtube.com/watch?v={video_id}'

            # Añadimos la información del video a la lista de videos
            videos.append({
                'Título': video_title,
                'Descripción': video_description,
                'Visualizaciones': views,
                'Likes': likes,
                'Canal': channel_title,
                'Fecha de publicación': published_at.strftime('%Y-%m-%d'),
                'Enlace': video_link
            })

            # Incrementamos el contador de resultados
            total_results += 1

            # Comprobamos si hemos alcanzado el límite máximo de resultados
            if max_results and total_results >= max_results:
                return videos

        # Comprobamos si hay más páginas de resultados
        if 'nextPageToken' in response:
            next_page_token = response['nextPageToken']
        else:
            break

    return videos

if __name__ == "__main__":
    query = "operacion triunfo"
    max_results = None  # None para obtener todos los resultados disponibles
    resultados = buscar_videos(query, max_results)

    # Convertimos los resultados a un DataFrame de pandas
    df = pd.DataFrame(resultados)

    # Guardamos el DataFrame en un archivo Excel
    df.to_excel('resultados_operacion_triunfo3.xlsx', index=False)
