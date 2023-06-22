""" Se tiene la siguiente lista ["gato", "perro", "elefante", "jirafa", "tigre"]
Crear una lista de números donde cada número es la longitud de una palabra. """

animales = ["gato", "perro", "elefante", "jirafa", "tigre"]

for i in animales:
    len(i)
    largo = [len(i)]
    print(largo)


longitudes = []
for i in range(len(animales)):
    longitudes.append(len(animales[i]))

print(longitudes)