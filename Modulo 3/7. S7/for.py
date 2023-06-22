#ciclo for
#Se utiliza para el recorrido de datos en listas, tuplas, diccionarios, set, string
#Se utiliza el metodo range() para obtener el rango hasta donde se debe recorrer
#Se utliza el metodo len() para obtener el tamaño de la estructura que se recorre

#indice [0, 1, 2, 3, 4, 5] desde 0 a n-1 siendo n la cantidad de elementos
lista = [1, 2, 3, 4, 5, 6] #lista con 6 elemtnos

#Recorriendo o conociento los elementos
for item in lista:
    print("Recorriendo el elemento de la lista",item)
    
#Recorriendo o conociendo el indice de la lista
for item in range(len(lista)):
    print("recorriendo el indice de la lista ",item)
    print("Recorriendo el elemtno de la lista ",lista[item])
    
#Recorriendo o conociendo el indice de la lista
for item in lista:
    print("Recorriendo el indice de la lista ",lista.index(item))
    

""" Diccionario """

diccionario = {"a":1, "b":2, "c":3, "d":4, "e":5, "f":6}

#obteniendo el valor de una key
for item in diccionario:
    print("Obteniendo el valor de la clave ",item)

#obteniendo el value de una clave
for item in diccionario:
    print("Obteniendo el valor ",diccionario[item])

#obteniendo solo los valores
for i in diccionario.values():
    print("Obteniendo el valor", i)

#obteniendo solo los key
for temp in diccionario.items():
    print("Obteniendo el elmento con clave:valor", temp)