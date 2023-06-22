
#? Crear una lista con 10 números enteros, recorrerla haciendo uso de la sentencia for
#? e imprimir en pantalla el valor de cada elemento indicando si es par, impar o cero.


lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] #lista con 6 elemtnos

#Recorriendo o conociento los elementos
for item in lista:
    if item == 0:
        print(f"El numero {item} es 0")
    elif item % 2 == 0:
        print(f"El numero {item} es par")
    else:
        print(f"El numero {item} es impar")