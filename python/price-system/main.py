# importando modulos internos
from menuFunctions import *
from functions import *

# variables
userMainOption = 0
userPriceOption = 0
userStatisticOption = 0

# Bucle del programa
while userMainOption != 5:
    # Opciones de menu principal
    printMainMenu()
    userMainOption = int(input('\n[user] Escoja una opcion [1 - 5]: '))

    if userMainOption == 1:
        # Ejecutnado precios aleatorios
        preciosAleatorios()

    if userMainOption == 2:
        # Bucle para el filtrado de precios
        while userPriceOption != 4:
            # Opciones del menu
            printPriceSort()
            userPriceOption = int(input('\n[user] Escoja una opcion [1 - 4]: '))

            if userPriceOption == 1:
                # Filtrando productos menores a $800.000
                filtradoPrecios(0, 800000)

            if userPriceOption == 2:
                # Filtrando productos entre $800.000 y $2.000.000
                filtradoPrecios(800000, 2000000)

            if userPriceOption == 3:
                # Filtrado de productos superior a $2.000.000
                filtradoPrecios(2000000, 2500000)

        # Habilita nuevamente la opcion filtrado de precios
        userPriceOption = 0

    if userMainOption == 3:
        # Bucle para las estadisticas
        while userStatisticOption != 5:
            # Opciones del menu
            printStatisticSort()
            userStatisticOption = int(input('\n[user] Escoja una opcion [1 - 5]: '))

            if userStatisticOption == 1:
                # Averiguamos el precio mas alto
                precioMasAlto()

            if userStatisticOption == 2:
                # Averiguamos el precio mas bajo
                precioMasBajo()

            if userStatisticOption == 3:
                # Obtenemos el promedio de precios
                promedioPrecios()

            if userStatisticOption == 4:
                # Obtenemos la media geometrica
                # q diablos es esto? xd, pq pediria algo asi...
                mediaGeometrica()

        # Habilita nuevamente la opcion estadisticas
        userStatisticOption = 0

    if userMainOption == 4:
        # Obtenemos el reporte segun las reglas de negocio
        obtenerReporte()

# Salida del programa
printCloseProgram()
