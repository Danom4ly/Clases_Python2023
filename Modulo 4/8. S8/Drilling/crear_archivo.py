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
# crear archivo si no se encuentra


def crear_archivo():
    try:
        file = open('informacion.dat', 'x')  # crear el archivo
        file.close()  # cerrar el archivo
    except FileExistsError:
        print("El archivo informacion.dat ya existe, ha sido creado previamente")


def leer_archivo():
    try:
        with open('informacion.dat', 'r') as file:
            datos = file.readlines()
            for linea in datos:
                print(linea.strip())
    except FileNotFoundError:
        print("No se encuentra el archivo.")


def escribir_archivo(lista):
    try:
        with open('informacion.dat', 'w') as file:
            for dato in lista:
                file.write(dato+"\n")

    except FileNotFoundError:
        print("No se encuentra el archivo a escribir.")


lista = ["Datos de información en la línea 1", "Datos de información en la línea 2",
        "Datos de información en la línea 3", "Datos de información en la línea 4", "Datos de información en la línea 5"]
crear_archivo()
escribir_archivo(lista)
leer_archivo()
