""" La resistencia dentro de un circuito paralelo se calcula como:

RT= 1/((1 /R1)+(1/R2)+(1/R3)+(1/Rn))

Donde:
● RT es la resistencia total.
● R1 es la resistencia 1.
● R2 es la resistencia 2.
● R3 es la resistencia 3.
● Rn la n-ésima resistencia.

Realizar el código en Python para calcular la resistencia total del circuito. """

""" r1 = float(input("Ingrese la Resistencia 1 : "))
r2 = float(input("Ingrese la Resistencia 2 : "))
r3 = float(input("Ingrese la Resistencia 3 : "))
rT = (1/((1/r1)+(1/r2)+(1/r3)))

print("La resistancia total es: {:.3f}".format(rT))
"""


""" Validar el ingresao de la resistencia, que sea mayor que 0, controlar error y utilizar funciones """

#Funcion para validar el ingreso de la resistencia en float.
def validate_input_float(texto):
    while True:
        try:       
            r = float(input(texto)) #float (), str(), int() casteo o transformacion, conversion del tipo de dato
            if r > 0:
                return r
            else:
                print("El valor es menor a 0")
        except Exception as e:
            print("Ha ocurrido un error en el ingreso de la resitencia",e)
            print("ingrese de nuevo el valor de la resistencia")

# Llamada a funcion o invocando
r_1 = validate_input_float("Ingrese la Resistencia 1 : ")
r_2 = validate_input_float("Ingrese la Resistencia 2 : ")
r_3 = validate_input_float("Ingrese la Resistencia 3 : ")

# Calcular la resistencia total
resistencia_total = (1/((1/r_1)+(1/r_2)+(1/r_3)))

# Imprimir la resistencia total en consola
print("La resistencia total es de", resistencia_total)