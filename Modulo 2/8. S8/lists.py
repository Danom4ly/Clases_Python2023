""" listas, colecciones de daots son llamadas tambien arreglos
se definen por [] corchetes
se definen utilizando la funcion list() """

#indices desde 0 a n-1, siendo n la cantidad de elementos
#indices[0, 1, 2, 3, 4, 5]
lista = [1, 2, 3, 4, 5, 6] #definiendo una lista con valores 1, 2, 3, 4, 5, 6
otra_lista = [] #definiendo una lista vacia
otra_lista = list() #defininendo una lista vacia
otra_lista = [31,1.72,"Fulanito","Perez"] #definiendo una lista

#acceder a la longitud o largo de la lista con funcion len()
print("Longitud de la lista, ",len(lista))
print("Longitud de otra_lista, ",len(otra_lista))

#conocer el tipo de dato
print("El tipo de dato de lista es: ",type(lista)) #<class 'list'>

#acceder a los elementos de la lista a traves de su indice
print("Elemento en el indice 0 de la lista: ",lista[0])
print("Elemento en el indice -1 de la lista: ",lista[-1])

#contar los elementos existentes de la lista con la funcion count() dado un elemento a contar, ej nombre_lista.count(elemento_a_contar)
print("Cantidad de veces que se repite el 1 en la lista: ",lista.count(1))

#acceder al indice de un elemento de la otra_lista con la funcion index()
print("Indice del elmento 2 en la otra_lista: ",otra_lista.index("Fulanito"))

#desempaquetar elementos de la lista en variables
edad, altura, nombre, apellido = otra_lista
print("Edad: ", edad)
print("Altura: ", altura)
print("Nombre: ", nombre)
print("Apellido: ", apellido)

#crear, insertar, actualizar y eliminar elementos de la lista
#crear un nuevo elemento en la lista
lista.append(7)
print("La lista es: ",lista)
lista.append("Arroz")
print("La lista es: ",lista)

#insertar elemento en la lista con funcion insert(index,elemento_insertar)
lista.insert(6,8)
print("La lista es: ",lista)

#actualizar elemento en la lista nombre_lista[indice_actualizar]
lista[6] = 7
lista[7] = 8
print("La lista es: ",lista)

#remover el elemento
lista.remove("Arroz")
print("La lista es: ",lista)

#algunas funciones de la lista
#count(), len(), index(), insert(), remove(), pop(), sort(), reverse()

#funcion pop(indice) por default "hace estallar" remueve el ultimo elemento de la lista
lista.pop()
print("La lista es: ",lista)

#funcion sort() ordena los elementos de la lista, reverse=True reverse=false
# otra_lista.sort() #[31,1.72,"Fulanito","Perez"] no permite ordenar listas con varios elementos de difrentes tipo
lista.sort(reverse=True)
print("La lista es: ",lista)

#funcion reverse() los ultimos elementos cambian a ser primero y los primero cambian a ser último
lista.reverse()
print("La lista es: ",lista)