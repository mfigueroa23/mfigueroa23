import requests as req
import pandas as pd

# Puedes obtener una API Key desde https://console.developers.google.com/
apiKey='' # API Key de YouTube Data API v3
channelId='UC_TVqp_SyG6j5hG-xVRy95A' # @Skirllex

url = f'https://www.googleapis.com/youtube/v3/channels?part=snippet,statistics,brandingSettings&id={channelId}&key={apiKey}'

res = req.get(url)
if res.status_code == 200:

    data = res.json()
    item = data['items'][0]

    snippet = item['snippet']
    statistics = item['statistics']
    branding_settings = item['brandingSettings']

    datos_canal = {
        'Nombre del Canal': [snippet['title']],
        'Descripción': [snippet.get('description', '')],
        'Fecha de Creación': [snippet['publishedAt']],
        'Pais': [snippet.get('country', '')],
        'Suscriptores': [statistics.get('subscriberCount', 'Privado')],
        'Videos Subidos': [statistics['videoCount']],
        'Vistas Totales': [statistics['viewCount']],
        'Imagen del Banner': [branding_settings['image'].get('bannerExternalUrl', 'No disponible')]
    }

    data_frame = pd.DataFrame(datos_canal)
    data_frame.to_excel('datos_canal.xlsx', index=False)
    print("Datos del canal guardados en 'datos_canal.xlsx'")

else:
    print(f"Error al obtener los datos del canal: {res.status_code}")
    print(res.text)
