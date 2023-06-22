""" 
Crear una función que acepte 3 números como parámetros, 
sume todos los valores, y adicionalmente reste el segundo y tercer parámetro al primero.
Al invocar la función, debemos pasarle los parámetros en forma de lista.
Esta devolverá ambos resultados en una tupla. Los resultados se deben imprimir en pantalla.
"""
#?Importar bibliotecas
import math


#?Definir Funciones
def sumatoria(n1,n2,n3):
    valor_final = ((n1+n2+n3))
    valor_final_2 = ((n1-n2-n3))
    
    return (valor_final, valor_final_2)

def valores_lista():
    n1= input("Valor 1: ")
    n2= input("Valor 2: ")
    n3= input("Valor 3: ")

# Ciclo for para mostrar valor
""" a = 0
for n in resultado:
    a = a + 1
    print(f"Valor {a} : {n}")
"""
#?Imprimir función
print((sumatoria(1,2,3)))
print(type(sumatoria(1,2,3,)))

