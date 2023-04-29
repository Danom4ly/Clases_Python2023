""" Tenemos una lista de números
[3, 5, 2, 8, 1, 10]
Se requiere encontrar el primer número par en la lista utilizando un
bucle while. """

lista = [3, 5, 2, 8, 1, 10]

i = 0

while i < len(lista):
    if lista[i] % 2 == 0:
        print("El primer número par es ", lista[i]) # i dentro de la lista
        break
    i = i+1
else:
    print("No se encontraron números pares")