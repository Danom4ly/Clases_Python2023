""" Se tiene la siguiente lista de nümeros:
numeros = [3, 5, 2, 8, 1, IO]
Calcular la suma de todos los nümeros de la lista utilizando un bucle while. """

numeros = [3, 5, 2, 8, 1, 10]

i = 0

suma = 0

while i < len(numeros):
    suma = suma + numeros[i]
    i=i+1

print("La suma de la lista es",suma)