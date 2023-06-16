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

#Crear archivo
def crear_archivo():
    try:
        file = open('informacion.dat','w') #Crear el archivo y se apertura
        print(file.readlines())
        file.close() #Cerrar el archivo
    except FileExistsError:
        print("Error: El archivo se encuentra creado")
    except Exception as e:
        print(f"Error: {e}")
        
crear_archivo()