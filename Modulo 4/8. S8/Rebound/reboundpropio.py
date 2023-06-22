""" 
Diseñe un programa en Python que cree un archivo si no se encuentra; en caso de existir el
archivo, debe reflejar un mensaje que especifica que ya se encuentra el archivo previamente
creado.
El archivo por crear debe llamarse informacion.dat. el cual contiene lo siguiente:
Datos de información en la línea 1
Datos de información en la línea 2
Datos de información en la línea 3
Datos de información en la línea 4
Datos de información en la línea 5 
"""

def crear_file():
    try:
        with open("informacion.dat","r") as file:# apertura y cierra el archivo, se puede establecer el tipo de apertura, r es para leer
            informacion = file.readlines() #retorna una lista de tipo str
            print("informacion.dat ya creado")
    except FileNotFoundError:
        with open("informacion.dat","w") as file:
            informacion = ["Datos de información en la línea 1\nDatos de información en la línea 2\nDatos de información en la línea 3\nDatos de información en la línea 4\nDatos de información en la línea 5"]
            file.writelines(informacion) # Escribir el archivo si no existe, w es para escribir
            print("Error: Informacion no ha sido encontrado, informacion.dat creado")
    return informacion

crear_file()