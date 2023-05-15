""" Tienes la siguiente lista de números:
[45, 23, 67, 89, 12, 56, 78, 90]
Encontrar el número más grande en la lista utilizando un bucle for. """

lista = [45, 23, 67, 23, 12, 56, 78, 90]

mayor = lista[0]
menor = lista[0]
repetido = []

for elemento in lista:
    if elemento > mayor:
        num = elemento
    if elemento < menor:
        menor = elemento
    if lista.count(elemento) > 1 and elemento not in repetido :
        repetido.append(elemento)

print(mayor)
print(menor)
print(repetido)