# Importando librerias
import pandas as pd
import matplotlib.pyplot as plt
from difflib import get_close_matches
from datetime import datetime
import unicodedata

# Cargando los datos desde el dataset de origen
usersStreamingTime = pd.read_csv("data.csv")

# Eliminacion de registros vacios en el mismo dataframe de pandas
usersStreamingTime.dropna(inplace=True)

# Eliminando columnas innecesarias
cols_eliminar = ['Señal Distintiva', 'Comuna']
for col in cols_eliminar:
    if col in usersStreamingTime.columns:
        usersStreamingTime.drop(columns=[col], inplace=True)

# Lista de meses
meses_correctos = (
    "enero", "febrero", "marzo", "abril", "mayo", "junio",
    "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"
)

# Lista de regiones con acentos correctos
regiones_chile = (
    "Región de Arica y Parinacota",
    "Región de Tarapacá",
    "Región de Antofagasta",
    "Región de Atacama",
    "Región de Coquimbo",
    "Región de Valparaíso",
    "Región Metropolitana de Santiago",
    "Región del Libertador General Bernardo O'Higgins",
    "Región del Maule",
    "Región de Ñuble",
    "Región del Biobío",
    "Región de La Araucanía",
    "Región de Los Ríos",
    "Región de Los Lagos",
    "Región de Aysén del General Carlos Ibáñez del Campo",
    "Región de Magallanes y de la Antártica Chilena"
)

# Función para quitar acentos
def quitar_acentos(texto):
    if not isinstance(texto, str):
        return texto
    return ''.join(c for c in unicodedata.normalize('NFD', texto) if unicodedata.category(c) != 'Mn')

# Función para limpiar datos
def limpiar_datos(df):
    # Eliminar espacios extra en todos los textos
    df = df.map(lambda x: x.strip() if isinstance(x, str) else x)
    
    # Corregir nombres de meses
    if "Mes" in df.columns:
        def corregir_mes(m):
            if not isinstance(m, str):
                return m
            m = m.lower().strip()
            cercano = get_close_matches(m, meses_correctos, n=1, cutoff=0.6)
            return cercano[0] if cercano else m
        df["Mes"] = df["Mes"].map(corregir_mes)
    
    # Normalizar regiones y acentos correctos
    if "Región" in df.columns:
        def corregir_region(r):
            if not isinstance(r, str):
                return r
            r = r.strip()
            r_sin_acento = quitar_acentos(r.lower())
            regiones_sin_acento = [quitar_acentos(reg.lower()) for reg in regiones_chile]
            cercano = get_close_matches(r_sin_acento, regiones_sin_acento, n=1, cutoff=0.6)
            if cercano:
                idx = regiones_sin_acento.index(cercano[0])
                return regiones_chile[idx]
            return r
        df["Región"] = df["Región"].map(corregir_region)
    
    return df

# Aplicando limpieza de datos
data = limpiar_datos(usersStreamingTime)

# Mapear meses de texto a número
mes_map = {
    "enero": 1, "febrero": 2, "marzo": 3, "abril": 4, "mayo": 5, "junio": 6,
    "julio": 7, "agosto": 8, "septiembre": 9, "octubre": 10, "noviembre": 11, "diciembre": 12
}
data["Mes_num"] = data["Mes"].str.lower().map(mes_map)

# Crear columna Fecha
data["Fecha"] = pd.to_datetime(
    dict(year=data["Año"], month=data["Mes_num"], day=data["Día"]),
    errors="coerce"
)

# Borramos las columnas originales
data.drop(columns=["Año", "Mes", "Mes_num", "Día"], inplace=True)

# Filtrar solo fechas hasta hoy
hoy = pd.Timestamp(datetime.now().date())
data = data[data["Fecha"] <= hoy]

# Filtrar filas con RUT válido
data = data[data['Rut'].str.len().between(9, 10) & data['Rut'].str.contains('-')]

# Función para obtener los millones del RUT
def millones_validos(rut):
    rut_base, _ = rut.split('-')
    millones = int(rut_base[:-6]) if len(rut_base) > 6 else 0
    return 1 <= millones <= 27

data = data[data['Rut'].apply(millones_validos)]

# Rango de edad
rangos_edad = {
    "Menor de Edad (0 - 18 años)": 0,
    "Adulto Joven (18 - 35 años)": 0,
    "Adulto (35 - 60 años)": 0,
    "Adulto Mayor (60 años o más)": 0
}

# Clasificación por RUT
for index, row in data.iterrows():
    rut_base = row['Rut'].split('-')[0]
    millones = int(rut_base[:-6]) if len(rut_base) > 6 else 0

    if 1 <= millones <= 6:
        rangos_edad["Adulto Mayor (60 años o más)"] += 1
    elif 7 <= millones <= 15:
        rangos_edad["Adulto (35 - 60 años)"] += 1
    elif 16 <= millones <= 21:
        rangos_edad["Adulto Joven (18 - 35 años)"] += 1
    elif 22 <= millones <= 27:
        rangos_edad["Menor de Edad (0 - 18 años)"] += 1

# Estadística descriptiva
print("\n[i] Estadística Descriptiva:")
cols = ['netflix', 'youtube', 'spotify']
print("\n1- Media:\n", data[cols].mean())
print("\n2- Mediana:\n", data[cols].median())
print("\n3- Moda:\n", data[cols].mode().iloc[0])
print("\n4- Desviación estándar:\n", data[cols].std())

# Gráfico 1: Servicio más escuchado
servicios_totales = data[cols].sum()
plt.figure(figsize=(6, 4))
servicios_totales.plot(kind="bar", color=["red", "blue", "green"])
plt.title("Servicios más escuchados")
plt.ylabel("Tiempo total de uso")
plt.xlabel("Servicios")
plt.tight_layout()
plt.savefig("servicios_mas_escuchados.jpg")
plt.close()

# Agregar columnas para Rango Etario
data["Millones"] = data["Rut"].str.split("-").str[0].str[:-6].astype(int)
data["Rango Etario"] = pd.cut(
    data["Millones"], bins=[0, 6, 15, 21, 27],
    labels=[
        "Adulto Mayor (60 años o más)",
        "Adulto (35 - 60 años)",
        "Adulto Joven (18 - 35 años)",
        "Menor de Edad (0 - 18 años)"
    ]
)

# Gráfico 2: Rango etario vs tiempo de servicios
rango_servicios = data.groupby("Rango Etario")[cols].sum()
plt.figure(figsize=(8, 5))
for servicio in cols:
    plt.plot(rango_servicios.index, rango_servicios[servicio], marker="o", label=servicio)
plt.title("Rangos Etarios vs Tiempo en Servicios")
plt.ylabel("Tiempo total de uso")
plt.xlabel("Rango Etario")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig("rango_etario_vs_servicios.jpg")
plt.close()

# Gráfico 3: Regiones vs servicios
region_servicios = data.groupby("Región")[cols].sum()
region_servicios.plot(kind="bar", stacked=True, figsize=(10, 6))
plt.title("Regiones vs Servicios más escuchados")
plt.ylabel("Tiempo total de uso")
plt.xlabel("Regiones")
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig("regiones_vs_servicios.jpg")
plt.close()
