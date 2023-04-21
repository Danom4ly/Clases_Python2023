#listas en python
#estructura para almacenar datow con un orde especifico de inseccion

lista = [1,2,3,4]
lista_diferentes_valores = [1,"2",3,"4",1.5,True,False,lista]

print(lista_diferentes_valores)#[1, '2', 3, '4', 1.5, True, False, [1, 2, 3, 4]]

#para acceder a los valores de un arreglo se utilizan los indices
#0 a n-1, pero tambien pueden ser negativos

print(lista[0]) #accediendo al indice 0 de la lista, 1
print(lista[-1]) #accediendo al indice -1 de la lista 4

#algunos metodos de la listas
#agergar, anexar valor
#nombre append()
lista.append(5)
print(lista)

#remove
lista.remove(2)
print(lista)

#pop elimina por indice
a = lista.pop(1)
print(a)
print(lista)

#inserccion por indice
lista.insert(1,2)
print(lista)

#indice por elemento
indice = lista.index(2)
print(indice)


