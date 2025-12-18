import requests
import json
import pandas as pd

latitude = -33.45
longitude = -70.65

url_clima = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
response = requests.get(url_clima)
wether_data = response.json()

current_weather = wether_data.get('current_weather', {})
print("Clima actual:", current_weather)

wether_data_es = {
    'temperatura': current_weather.get('temperature'),
    'velocidad_viento': current_weather.get('windspeed'),
    'codigo_clima': current_weather.get('weathercode'),
    'es_dia': current_weather.get('is_day'),
    'intervalo': current_weather.get('interval'),
    'hora': current_weather.get('time')
}

secure_lat = str(latitude).replace('.', '_').replace('-', 'neg')
secure_lon = str(longitude).replace('.', '_').replace('-', 'neg')

firebase_path = f"clima/lat{secure_lat}_lon{secure_lon}.json"
firebase_url = ""
firebase_full_url = firebase_url + firebase_path

firebase_response = requests.put(firebase_full_url, data=json.dumps(wether_data_es))
print("Datos enviados a Firebase:", firebase_response.status_code, firebase_response.text)

excel_data = pd.DataFrame([wether_data_es])
excel_name = f"clima_{secure_lat}_{secure_lon}-Santiago-Chile.xlsx"
excel_data.to_excel(excel_name, index=False)
print(f"Datos guardados en el archivo Excel: {excel_name}")
