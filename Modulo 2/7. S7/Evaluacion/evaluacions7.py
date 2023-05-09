""" Recorrer los datos numéricos que se encuentran dentro de la siguiente lista de listas:
[[1,2,3], [0,4,5], [4,0,1], [6,5,4]]
Se debe imprimir cada dato de las listas en pantalla con las siguientes excepciones:
• Si el primer nümero de la sublista es cero, omitir la impresiön de toda la sublista.
• Si existe un cero en cualquier otra posición, omitir solo la impresión del cero. """

listas = [[1,2,3], [0,4,5], [4,0,1], [6,5,4]]

for lista in listas:
    if lista[0] == 0:
        continue
    for num in lista:
        if num == 0:
            continue
        print(num)
