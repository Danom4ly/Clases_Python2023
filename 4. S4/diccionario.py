#ordenados por clave y valor
#diccionarios, es una coleccion de elemtnos
#declaracion con llaves {} o con la funcion dict()

estudiantes = {
    #clave:valor
    "fulanito":25,
    "Maria":22,
    "Jose": 40,
    "Marta": 30
}

print(estudiantes)

#acceder al valor de una clave
# diccionario[clave]
print(estudiantes["fulanito"])

#remover clave de un diccionario
del estudiantes["fulanito"]
print(estudiantes)

#obtener todas las claves de un diccionario
claves = estudiantes.keys()
print(claves)

#obtener todos los valores de un diccionario
valores = estudiantes.values()
print(valores)

#borrar un diccionario
estudiantes.clear()
