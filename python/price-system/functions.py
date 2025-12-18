# imports de librerias
import random
import math
import csv

# variables
productos = ["Televisor", "Lavadora", "Refrigerador", "Microondas", "Computadora", "Celular", "Impresora", "Cafetera", "Licuadora", "Ventilador"]
listadoProductos = []
listadoPrecios = []

def preciosAleatorios():
    print('\n[system] Generando valores aleatorios...')
    for nombreProducto in productos:
        precioAleatorio = random.randint(300000, 2500000)
        producto = {nombreProducto: precioAleatorio}
        listadoProductos.append(producto)
        listadoPrecios.append(precioAleatorio)
    print('[system] Valores generados con éxito')

def filtradoPrecios(precioMinimo, precioMaximo):
    print(f'\n[system] Fitrando productos con precios desde ${precioMinimo} hasta ${precioMaximo} ...\n')
    print('[system] Listado de productos:')
    for producto in listadoProductos:
        for key in producto:
            if(producto.get(key) >= precioMinimo and producto.get(key) <= precioMaximo):
                print(f'{key}: ${producto.get(key)}')

def precioMasAlto():
    print('\n[system] Obteniendo el producto con el precio mas alto...\n')
    nombreProducto = None
    valorMasAlto = 0
    for producto in listadoProductos:
        for key in producto:
            if producto.get(key) > valorMasAlto:
                valorMasAlto = producto.get(key)
                nombreProducto = key
    if nombreProducto != None:
        print(f'[system] {nombreProducto} es el producto con el mayor precio: ${valorMasAlto}')

def precioMasBajo():
    print('\n[system] Obteniendo el producto con el precio mas bajo...\n')
    nombreProducto = None
    valorMasBajo = float('inf') # Numero infinito
    for producto in listadoProductos:
        for key in producto:
            if producto.get(key) < valorMasBajo:
                valorMasBajo = producto.get(key)
                nombreProducto = key
    if nombreProducto != None:
        print(f'[system] {nombreProducto} es el producto con el menor precio: ${valorMasBajo}')

def promedioPrecios():
    print('\n[system] Obteniendo el promedio de los precios...\n')
    promedio = sum(listadoPrecios) / len(listadoPrecios)
    print(f'[system] El promedio de precios es: ${promedio}')

def mediaGeometrica():
    print('\n[system] Obteniendo la media geometrica de los precios...\n')
    producto = 1
    totalItems = len(listadoPrecios)
    for precio in listadoPrecios:
        producto *= precio
    resultado = producto ** (1/totalItems)
    print(f'[system]: La media geometrica de los precios es: {resultado}')

def obtenerReporte():
    print(f'\n[system]: Armando reporte...\n')
    with open('reporte_precios.csv', mode = 'w', newline = '') as file:
        writer = csv.writer(file)
        writer.writerow(["Nombre Producto", "Precio Actual", "Descuento Promocios 10%", "Descuento Membresia 5%", "Precio Final"])
        i = 0
        for precio in listadoPrecios:
            descuentoPromocion = precio * 0.10
            descuentoMembresia = precio * 0.05
            precioFinal = precio - descuentoPromocion - descuentoMembresia
            writer.writerow([ productos[i], precio, descuentoMembresia, descuentoMembresia, precioFinal ])
            i += 1
    print('[system]: Reporte generado con exito')
