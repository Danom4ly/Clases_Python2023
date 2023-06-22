""" 
Se solicita crear un programa en Python que permita Ilevar el registro de los libros que han Sido prestados por una biblioteca.
Para ello, se pide crear un conjunto (set) con los nombres de los libros prestados.
A continuaci6n, se solicita imprimir en pantalla la cantidad total de libros prestados.
Finalmente, se debe crear Otro conjunto con los nombres de los libros que han sido devueltos y mostrar en pantalla los libros que aün no han sido devueltos. 
"""

libros_disponibles = {'Cien años de soledad', 'El amor en los tiempo del colera', 'La ciudad y los perros', 'La casa verde', 'El otoño dle patriarca', 'Rayuela', 'Pedro Paramo', 'La tregua'}
#print(libros_disponibles)
#print(len(libros_disponibles))

libros_prestados = set()
#print(type(libros_prestados))
#print(libros_disponibles)

libros_devueltos = set()
#print(type(libros_devueltos))
#print(libros_devueltos)

#Menu
#Mostrar libros_disponibles
#Mostrar libros_prestados
#Pedir libro en libros_disponible
#devolver libro en libros_prestados
#Mostrar libros_devueltos

while len(libros_disponibles) > 0:
    libro = input("Ingrese el libro que desea pedir: ")
    if libro in libros_disponibles:
        libros_prestados.add(libro)
        libros_disponibles.remove(libro)
        break
    else:
        print("El libro no se encuentra en el conjunto de libros disponibles")