"""
Se solicita crear un diccionario en Python para almacenar los precios
de diferentes productos en una tienda en línea.
"""

#? Funcion recorrer el diccionario e imprimir los productos cuyos precios son superiores a 50 dólares.
def recorrer_diccionario():
    for producto in precios:
        if precios[producto] > 50:
            print(producto)

#? Funcion calcular el precio total de los productos cuyos nombres empiezan con la letra 'C' y mostrarlo en pantalla.
def calcular_precio_total():
    total = 0
    for producto in precios:
        if precios[producto] > 0:
            total += precios[producto]
    print(total)

#? Las claves del diccionario serán los nombres de los productos y los valores serán los precios de los productos.

precios = {
'camisa': 30,
'pantalon': 50,
'zapatos': 80,
'calcetines': 10,
'chaqueta': 100
}

recorrer_diccionario()
calcular_precio_total()

