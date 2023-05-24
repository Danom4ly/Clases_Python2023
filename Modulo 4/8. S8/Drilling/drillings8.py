""" 
Partiendo de la actividad realizada en el Rebound Exercises, construya una función que lea el
contenido del archivo informacion.dat.
Teniendo como salida lo siguiente:
$ python ejercicio.py
El archivo informacion.dat ya existe, ha sido creado previamente
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

def leer_archivo():
    try:
        with open("informacion.dat","r") as file:
            datos = file.readlines()
            for linea in datos:
                print(linea,end="")
    except FileNotFoundError:
        print ("No se encuentra el archivo")

crear_file()
leer_archivo()