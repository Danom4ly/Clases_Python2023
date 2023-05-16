""" Se tiene el siguiente diccionario llamado ventas de una empresa que almacena las ventas mensuales de una empresa por producto
ventas = {
"producto_a": [100, 150, 200, 300, 250, 175, 125, 200, 300, 400, 500, 550],
"producto_b": [50, 75, 100, 125, 150, 175, 200, 225, 250, 275, 300, 325],
"producto_c": [200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750]
}
Calcular el total de ventas de cada producto. """


ventas = {
"producto_a": [100, 150, 200, 300, 250, 175, 125, 200, 300, 400, 500, 550],
"producto_b": [50, 75, 100, 125, 150, 175, 200, 225, 250, 275, 300, 325],
"producto_c": [200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750]
}

for producto, ventas_mensuales in ventas.items():
    total_ventas = sum(ventas_mensuales)
    print(f"El total de las ventas mensuales del {producto} es: {total_ventas}")


""" 
dict_ventas = {}
for producto, ventas_mensuales in ventas.items():
    dict_ventas[producto] = sum(ventas_mensuales)
print(dict_ventas) """