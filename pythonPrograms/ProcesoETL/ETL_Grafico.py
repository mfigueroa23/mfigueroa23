#importanmos libreria de pandas
import pandas as pd
#importamos libreria de MAtlotlib
import matplotlib.pyplot as plt 

#1. Definimios un metodo para extraer la informacion de un archivo
#primero parametro o argumentos "archivo_csv"
def extraer_datos(archivo_csv):
    #Leemos el arvhico CSV que extraemos
    datos = pd.read_csv(archivo_csv) #lee los diferentes tipos de textos 
    #retorno los datos
    return datos 

#2. Tranformamos la informacion del archivo
def transformar_datos(datos):
    #eliminamos los valores vacios o nulos del archivo
    #y calculamos totales ya gregamos columnas
    datos_transformados = datos.dropna().copy() # borra todo los datos vacios dropna # copy los datos 
    #calculamos el total
    datos_transformados['total'] = datos_transformados['cantidad'] * datos_transformados['precio']
    #calculamos del IVA 19% 
    datos_transformados['total_con_iva'] = datos_transformados['total'] * 1.19
    return datos_transformados

#3. Definimos una funcion para cargar los datos en un nuevo archivo csv
def cargar_datos(datos_transformados, archivo_destino):
    #guardo la informacion en el archivo
    datos_transformados.to_csv(archivo_destino, index=False) #tranformar el archivo  a csv

#ejecutamos el codigo
#definimos el archivo de origen y destino 
archivo_origen = 'datos_origen.csv'
archivo_destino = 'datos_destino.csv'

#Procesamos el ETL
#1. Extraemos la informacion del archivo
datos_extraidos = extraer_datos(archivo_origen)
#2. tranformamos los datos 
datos_transformados = transformar_datos(datos_extraidos)
#3. cargamos los datos
cargar_datos(datos_transformados, archivo_destino)
#imprimo un mensaje
print("proceso ETL completo 😁") #windosws + punto = emoticonos 


#creamos un grafico visual 
#definimos el tamaño del grafico
plt.figure(figsize=(12,7))
#definimos el tipo de grafico
plt.bar(datos_transformados['producto'], datos_transformados['total_con_iva'], color = 'red' )
plt.xlabel('Producto')
plt.ylabel('Total con IVA($)')
#agregamos estilo en el grafico
plt.grid(axis='y', linestyle='--', alpha=0.6)
#movemos los textos del eje x
plt.xticks(rotation=45, ha='right')
#mostramos el grafico
plt.show()
