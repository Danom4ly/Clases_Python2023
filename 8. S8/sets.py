"""
Set, colecion de daots, conjunto de datos
Se define utilizando la funcion set()
se puede definir con {} pero se inicializa como un diccionario
"""

#Definir un set
set_datos = set({10,20,15,4,3,2})
my_set = {} #se inicializa como un diccionario

#Verificar o ver el tipo de dato de un set
print("El tipo de dato de set_datos es:", type(set_datos)) #<class 'set'>
print("El tipo de dato de my_datos es:", type(my_set)) #<class 'dict'>

#Verificar el largo de un set, longitud con len(parametro)
print("Largo de set_datos es:", len(set_datos)) #6
print("Largo de my_set es:", len(my_set)) #0

#Agregar elementos a un set
set_datos.add(1)
print("set_datos: ", set_datos)

my_set = set() #inicializando un set vacio
my_set.add(2)

#No permite elementos repetidos
set_datos.add(1)
print("set_datos: ", set_datos)

#busqueda de elementos en un set
print("Busqueda del numero 10 en set_datos: ", 10 in set_datos)
print("Busqueda del numero 10 en set_datos: ", "Python" in set_datos)

#Remover elementos de un set
set_datos.remove(1)
print("set_datos: ", set_datos)

#removoer todos o borrar el set, limpiar
my_set.clear()
print("my_set: ", my_set)

del my_set #elimina el set, la variable my_set no existe
#!print("my_set: ", my_set) #name 'my_set' is not defined

#actualizar un set, funcion update(set_a_agregar)
set_datos.update({3,12,11,25})
print("set_datos: ", set_datos)

#otras operaciones
#union()
my_set = {50,100,200}
new_set = set_datos.union(my_set)
print("new_set: ", new_set)

#interseccion() #datos existentes dentro de dos set
interseccion_set = new_set.intersection(my_set)
print("interseccion_set: ", interseccion_set)

#difference()
diferencias_set = new_set.difference(my_set)
print("diferrence: ", diferencias_set)