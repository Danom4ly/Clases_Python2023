""" De la siguiente lista de precios de productos:
[25.50, 12.30, 36.40, 9.75, 15.20]
Calcular el precio total de la compra con un descuento del 10%. """

compra = [25.50, 12.30, 36.40, 9.75, 15.20]

comprdesc = sum(compra)*.90
print(f"su compra es {sum(compra)}")
print(f"y con el descuento del 10% queda el total de {comprdesc}")