
#! Tuplas, son colecciones de datos, se puede acceder por el indice del elemento
#! se definen con al funcion tuple()
#! se definen con parentesis nombre_tupla = ()

# Definir una tupla
tupla = 1, 2, 3, 4
tupla = tuple()
tupla = ()
print("tupla")

#indice van desde 0 a n-1 siendo n la cantidad de elementos
#indices(0 ,  1 ,   2  ,      3    )
tupla = (31,1.80,"Jose","Feliciano")

#acceder al tipo de dato de la tuple
print("El tipo de dato de la tupla es: ",type(tupla))

#acceder a los elementos de la tupla con los indices, nombre_tupla[indice]
print("El elemento en el indice 0 es: ",tupla[0])
print("El elemento en el indice -1 es: ",tupla[-1]) #indice negativo parta desde la ultima parte de la tupla, desde su ultimo elemento

#metodos de la tupla
#count(), index(indice)
print("El elemento 31 su cuenta es:",tupla.count(31)) #1
print(f"El elemento 31 su cuenta es: {tupla.count(31)}")
print("El elemento 31 su cuenta es: {} {}".format(tupla.count(31),"Valor Agregado"))

#funcion index(elemento)
indice_elemento = tupla.index("Feliciano")
print("El indice del elemento feliciano es: ",indice_elemento)

#subtuplas extraer elementos de una tupla
sub_tupla = tupla[0:3]
print(sub_tupla)
print(tupla[1:3])

#! No se pueden eliminar elementos

