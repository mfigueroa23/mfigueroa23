import kagglehub
import pandas as pd
import os
import shutil

# Descarga el dataset desde Kaggle
print("Descargando el dataset...")
dataset_path = kagglehub.dataset_download("itssuru/super-store")
current_dir = os.getcwd()
destination_dir = os.path.join(current_dir, "SuperStore")
shutil.move(dataset_path, destination_dir)

# Extrae los datos de DataSet
def extract_data(archivo_csv):
    print("Extrayendo datos del archivo CSV...")
    datos = pd.read_csv(archivo_csv)
    return datos

# Funcion para cargar los datos
def cargar_datos(datos, archivo_destino):
    print("Cargando datos al archivo destino...")
    datos.to_csv(archivo_destino, index=False)

# Funcion para las ganancias por envio
def sumar_ganancias_por_envio(df):
    print("Sumando ganancias por tipo de envío...")
    df_limpio = df.dropna()
    ganancias_por_envio = (df_limpio.groupby('Ship Mode')['Profit'].sum().reset_index().rename(columns={
        'Ship Mode': 'Tipo de Envio', 
        'Profit': 'Ganancias'
    }))
    return ganancias_por_envio

# Proceso ETL
datos = extract_data("SuperStore/SampleSuperstore.csv")
ganancias_por_envio = sumar_ganancias_por_envio(datos)
archivo_destino = "SuperStore/ganancias_por_envio.csv"
cargar_datos(ganancias_por_envio, archivo_destino)
