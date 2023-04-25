""" La resistencia dentro de un circuito paralelo se calcula como:

RT= 1/((1 /R1)+(1/R2)+(1/R3)+(1/Rn))

Donde:
● RT es la resistencia total.
● R1 es la resistencia 1.
● R2 es la resistencia 2.
● R3 es la resistencia 3.
● Rn la n-ésima resistencia.

Realizar el código en Python para calcular la resistencia total del circuito. """

r1 = float(input("Ingrese la Resistencia 1 : "))
r2 = float(input("Ingrese la Resistencia 2 : "))
r3 = float(input("Ingrese la Resistencia 3 : "))
rT = (1/((1/r1)+(1/r2)+(1/r3)))

print("La resistancia total es: {:.3f}".format(rT))
