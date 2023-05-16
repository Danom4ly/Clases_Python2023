""" simula un juego de adivinanza,
donde el jugador debe adivinar un número aleatorio generado por el programa.
El programa le dará pistas al jugador sobre si el número ingresado es mayor o menor que el número generado,
y seguirá pidiendo al jugador que ingrese un número hasta que adivine correctamente. """

import random

numero_generado = random.randint(0,10) #Genera un numero random entero
#? print(numero_generado)

print("""Bienvenido al juego de adivinanza
Deberas adivinar un numero entre el 0 al 10""")

adivinanza = 11
contador = 0
while adivinanza != numero_generado:
    adivinanza = int(input("Ingresa un numero del 0 al 10: "))
    contador += 1
    if adivinanza > numero_generado:
        print("El numero es mayor al numero a adivinar")
    elif adivinanza < numero_generado:
        print("El numero es menor al numero a adivinar")
    else:
        print("Has adivinado el numero correctamente al intento %d " % contador)

