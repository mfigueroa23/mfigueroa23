import pandas as pd
import matplotlib.pyplot as plt

# Variables
archivo_origen = 'ventas_ext_price_trimmed.csv'

# Extraer los datos
def extraer_datos(archivo_csv):
    datos = pd.read_csv(archivo_csv)
    return datos

# Funcion para cargar los datos
def cargar_datos(datos, archivo_destino):
    datos.to_csv(archivo_destino, index=False)

# Funcion para ver los productos vendidos en una tienda
def productos_vendidos_por_tienda(datos, tienda):
    # Filtrar los datos por la tienda especificada
    datos_tienda = datos[datos['tienda'] == tienda]
    # Agrupar por SKU y sumar la cantidad vendida
    productos_agrupados = datos_tienda.groupby('sku')['cantidad_vendida'].sum().reset_index()
    # Renombrar las columnas para mayor claridad
    productos_agrupados.columns = ['Producto', 'Cantidad Vendida']
    return productos_agrupados

# Funcion para ver las ganancias totales por tienda
def ganancias_totales_por_tienda(datos):
    # Crear una columna de ganancias (cantidad_vendida * precio)
    datos['ganancia'] = datos['cantidad_vendida'] * datos['precio']
    # Agrupar por tienda y sumar las ganancias
    ganancias_por_tienda = datos.groupby('tienda')['ganancia'].sum().reset_index()
    # Renombrar las columnas para mayor claridad
    ganancias_por_tienda.columns = ['Tienda', 'Ganancia Total']
    return ganancias_por_tienda

# Funcion para ver los productos totales vendidos y sus ganacias totales
def productos_y_ganancias_totales(datos):
    # Crear una columna de ganancias (cantidad_vendida * precio)
    datos['ganancia'] = datos['cantidad_vendida'] * datos['precio']
    # Agrupar por SKU y calcular la cantidad total vendida y las ganancias totales
    productos_agrupados = datos.groupby('sku').agg({'cantidad_vendida': 'sum', 'ganancia': 'sum'}).reset_index()
    # Renombrar las columnas para mayor claridad
    productos_agrupados.columns = ['Producto', 'Cantidad Vendida', 'Ganancia Total']
    return productos_agrupados

# Extraccion de los datos
datos_extraidos = extraer_datos(archivo_origen)

# Proceso ETL Productos vendidos por tienda
datos_transformados_tienda_A = productos_vendidos_por_tienda(datos_extraidos, 'Tienda A')
datos_transformados_tienda_B = productos_vendidos_por_tienda(datos_extraidos, 'Tienda B')
datos_transformados_tienda_C = productos_vendidos_por_tienda(datos_extraidos, 'Tienda C')
cargar_datos(datos_transformados_tienda_A, 'productos_vendidos_tienda_A.csv')
cargar_datos(datos_transformados_tienda_B, 'productos_vendidos_tienda_B.csv')
cargar_datos(datos_transformados_tienda_C, 'productos_vendidos_tienda_C.csv')

# Proceso ETL Ganancias totales por tienda
datos_transformados_ganancias = ganancias_totales_por_tienda(datos_extraidos)
cargar_datos(datos_transformados_ganancias, 'ganancias_totales_por_tienda.csv')

# Proceso ETL Productos y ganancias totales
datos_transformados_productos_ganancias = productos_y_ganancias_totales(datos_extraidos)
cargar_datos(datos_transformados_productos_ganancias, 'productos_y_ganancias_totales.csv')

# Grafico de pastel para los productos vendidos por tienda
def grafico_pastel_productos_vendidos(archivo_csv, tienda):
    datos = pd.read_csv(archivo_csv)
    plt.figure(figsize=(8, 8))
    plt.pie(datos['Cantidad Vendida'], labels=datos['Producto'], autopct='%1.1f%%', startangle=140)
    plt.title(f'Productos Vendidos en {tienda}')
    plt.savefig(f'productos_vendidos_{tienda}.png')

# Grafico de barras para las ganancias totales por tienda
def grafico_barras_ganancias_tienda(archivo_csv):
    datos = pd.read_csv(archivo_csv)
    plt.figure(figsize=(10, 6))
    plt.bar(datos['Tienda'], datos['Ganancia Total'], color='skyblue')
    plt.title('Ganancias Totales por Tienda')
    plt.xlabel('Tienda')
    plt.ylabel('Ganancia Total')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.savefig('ganancias_totales_por_tienda.png')

# Grafico de lineas para los productos y ganancias totales
def grafico_lineas_productos_ganancias(archivo_csv):
    datos = pd.read_csv(archivo_csv)
    plt.figure(figsize=(12, 7))
    plt.plot(datos['Producto'], datos['Ganancia Total'], marker='o', linestyle='-', color='green', label='Ganancia Total')
    plt.plot(datos['Producto'], datos['Cantidad Vendida'], marker='s', linestyle='--', color='orange', label='Cantidad Vendida')
    plt.title('Productos y Ganancias Totales')
    plt.xlabel('Producto')
    plt.ylabel('Valores')
    plt.legend()
    plt.grid(axis='y', linestyle='--', alpha=0.6)
    plt.savefig('productos_y_ganancias_totales.png')

# Llamadas a las funciones para generar los gráficos
grafico_pastel_productos_vendidos('productos_vendidos_tienda_A.csv', 'Tienda A')
grafico_pastel_productos_vendidos('productos_vendidos_tienda_B.csv', 'Tienda B')
grafico_pastel_productos_vendidos('productos_vendidos_tienda_C.csv', 'Tienda C')
grafico_barras_ganancias_tienda('ganancias_totales_por_tienda.csv')
grafico_lineas_productos_ganancias('productos_y_ganancias_totales.csv')
