#Importar la libreria de pandas y matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# 1. Funcion de Extraer la informacion
def extraer_datos(archivo_csv):
    #Pasamos el archivo pandas lo lee y lo guarda en la variable de datos
    datos = pd.read_csv(archivo_csv)
    return datos

# 2. Funcion para transformar los datos extraidos
def transformar_datos(datos):
    #Limpiamos las filas vacias y agregamos la columna del total y el total con iva
    datos_transformados = datos.dropna().copy()
    datos_transformados['total'] = datos_transformados['unidades'] * datos_transformados['valor_unitario']
    datos_transformados['total_con_iva'] = datos_transformados['total'] * 1.19
    return datos_transformados

# 3. Funcion para cargar los datos transformados
def cargar_datos(datos_transformados, archivo_destino):
    datos_transformados.to_csv(archivo_destino, index=False)
 
#Indicamos el archivo de entrada y salida
archivo_origen = 'datos_origen.csv'
archivo_destino = 'datos_destino.csv'

# Proceso ETL
datos_extraidos = extraer_datos(archivo_origen)
datos_transformados = transformar_datos(datos_extraidos)
cargar_datos(datos_transformados, archivo_destino)

# Agrupo productos y sumo el total más IVA
productos_agrupados = datos_transformados.groupby('producto')['total_con_iva'].sum().reset_index()

# Grafico de la informacion en lineas
plt.figure(figsize=(12, 7))
plt.plot(productos_agrupados['producto'], productos_agrupados['total_con_iva'], marker='o', linestyle='-', color='blue')

# Informacion del grafico
plt.title('Total por Producto con IVA')
plt.xlabel('Producto')
plt.ylabel('Total con IVA')
plt.grid(axis='y', linestyle='--', alpha=0.6)

# Mensaje de confirmacion
print("Proceso ETL Completado 😎")
plt.show()
