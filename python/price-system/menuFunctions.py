# importando objetos de opciones diponibles
from options import *

def printMainMenu():
    # Imprimiendo bienvenida
    print('\n--- Análisis de Precios de Productos ---\n')
    for key in mainOptions:
        print(f'{key}: {mainOptions.get(key)}')

def printCloseProgram():
    # Salida no tan vulgar del sistema ;)
    print('\n--- Programa cerrado con éxito ---\n')

def printPriceSort():
    # Imprimiendo opciones del menu
    print('\n--- Clasificar precios ---\n')
    for key in priceSort:
        print(f'{key}: {priceSort.get(key)}')

def printStatisticSort():
    # Imprimiendo opciones del menu
    print('\n--- Ver estadísticas ---\n')
    for key in statisticSort:
        print(f'{key}: {statisticSort.get(key)}')
