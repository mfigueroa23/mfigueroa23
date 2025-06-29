import pyodbc

class Conexion:

    def __init__(self, servidor, base_datos, usuario, contrasena):
        self.conexion = pyodbc.connect(
            f'DRIVER={{ODBC Driver 17 for SQL SERVER}};'
            f'SERVER={servidor};'
            f'DATABASE={base_datos};'
            f'UID={usuario};'
            f'PWD={contrasena};'
        )
        self.cursor = self.conexion.cursor()
    
    def insertar_pelicula(self, titulo, resumen, fecha_estreno):
        self.cursor.execute("INSERT INTO Peliculas(titulo, resumen, fecha_estreno) VALUES(?, ?, ?)", titulo, resumen, fecha_estreno)

    def guardar(self):
        self.conexion.commit()

    def cerrar(self):
        self.cursor.close()
        self.conexion.close()
