""" Se tiene una lista de nombres de personas
["Juan", "María", "Pedro", "Ana", "Roberto", "Lucía", "Luisa"]
Imprimir los nombres que tienen una longitud mayor que 5 caracteres. """

nombresPersonas = ["Juan", "María", "Pedro", "Ana", "Roberto", "Lucía", "Luisa"]

for nombre in nombresPersonas:
    if len(nombre) > 5:
        print(nombre)