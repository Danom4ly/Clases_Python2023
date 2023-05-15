""" 
Crear una función que sume dos números, otra que reste dos números, otra que multiplique dos números, y otra que divida dos números.
Adicionalmente, crear una función que acepte dos números como parámetros y regrese el resultado en forma de tupla
de su suma, resta, multiplicación y división.
Los resultados se deben almacenar en un diccionario, cuyas claves serán: Suma, Resta, Multiplicación y División,
y los valores de cada clave serán los resultados obtenidos con la función creada anteriormente. 
"""
#?import biblioteca
import math

#? Definciendo funciones
def suma(n1,n2):
    suma = n1 + n2
    return suma

def resta(n1,n2):
    resta = n1 - n2
    return resta

def multiplicacion(n1,n2):
    multiplicacion = n1 * n2
    return multiplicacion

def división(n1,n2):
    división = n1 // n2
    return división

def tupla(n1,n2):
    return(suma(n1,n2),resta(n1,n2),multiplicacion(n1,n2),división(n1,n2))

resultado = tupla(2,2)
print(resultado)

resultados_totales = {
    "Suma": resultado[0],
    "Resta": resultado[1],
    "Multiplicación": resultado[2],
    "División": resultado[3]
}

print(resultados_totales)