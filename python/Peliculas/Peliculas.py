import requests
from Conexion import Conexion

API_KEY = ''
pelicula = ''
url = f'https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={pelicula}&language=es-ES'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    results = data.get('results', [])
    if not results:
        print("No se encontró peliculas.")
    else:
        db = Conexion(servidor='10.0.6.39', base_datos='PeliculaDB_MarcoFigueroa', usuario='estudiante', contrasena='Informatica-164')
        for pelicula in results:
            titulo = pelicula.get('title', 'Sin título')
            resumen = pelicula.get('overview', 'Sin resumen')
            fecha = pelicula.get('release_date', None)
            print(f'Pelicula encontrada: {titulo} | {fecha}')
            db.insertar_pelicula(titulo, resumen, fecha)
        db.guardar()
        db.cerrar()
        print("Peliculas guardadas en la base de datos.")
else:
    print(f"Error al realizar la solicitud: {response.status_code}")
    print(response.text)
