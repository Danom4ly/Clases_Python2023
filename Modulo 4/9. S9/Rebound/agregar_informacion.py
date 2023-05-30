

def agregar_info(texto):
    try:
        with open("informacion.dat", "a", encoding="UTF-8") as file:
            file.write(texto+"\n")
    except FileNotFoundError:
        print("ERROR: No se encontro el archivo de informacion")
    except Exception as e:
        print("ERROR: ",e)

agregar_info("Hola Mundo")
agregar_info("Este en una nueva línea en el archivo")
agregar_info("agregando la segunda línea del archivo")
agregar_info("finalizando la línea agregada")