import random

#! Juego 1

palabras_secretas = ["arroz", "pollo", "pure", "choclo", "chorrillana"]
adivinar = random.choice(palabras_secretas)
intentos = 5
turno = 0
ingreso = ""
while adivinar != ingreso and turno < intentos:
    ingreso = input("ingrese la palabra: ")
    turno += 1
    if ingreso == adivinar:
        print(f"Ha encontrado la palabra secreta en {turno} turnos")
    elif turno == intentos:
        print(f"no tiene más intentos, la palabra secreta era {adivinar}")
    else:
        print(f"sigue intentando, vas en el turno {turno} de 5")


#! Juego 2

palabra_secreta = "python"

def comprobar_adivinanza(palabra, adivinanza):
    letras_correctas = 0
    for letra in adivinanza:
        if letra in palabra:
            letras_correctas += 1
    return letras_correctas

while True:
    adivinanza = input("adivina la palabra secreta: ")
    letras_correctas = comprobar_adivinanza(palabra_secreta, adivinanza)
    if letras_correctas == len(palabra_secreta):
        print("adivinaste la palabra")
        break
    else:
        print("solo adivinaste", letras_correctas, " letras")

#! juego 3

personas = ["Natalia", "Joaquin", "Onofrio", "Adrian", "Victor", "Eduardo", "Federico", "Aaron", "Ignacio", "Camilo"]

palabra = random.choice(personas).lower()

adivinado = []

vidas = 6

# Función para mostrar el estado actual del juego
def mostrar_estado(adivinado, palabra):
    """    Muestra el estado actual del juego, con las letras adivinadas   
    y las letras que faltan por adivinar    """    
    for letra in palabra:
        if letra in adivinado:
            print(letra, end=" ")
        else:
            print("_", end=" ")
    print("\n")
    
# Comenzar el juego
print("¡Bienvenido al juego del ahorcado, versiòn compañeros del Bootcamp!\n")

mostrar_estado(adivinado, palabra)


while True:
    
    letra = input("Introduce una letra: ")
    
    adivinado.append(letra)
    
    if letra not in palabra:
        vidas -= 1        
        print("La letra", letra, "no está en el nombre del compañero. Te quedan", vidas, "vidas.")
        if vidas == 0:
            print("¡Has perdido! el compañero era", palabra)
            break    
    else:
        print("¡La letra", letra, "está en el nombre!")
    
    # Mostrar el estado actual del juego   
    mostrar_estado(adivinado, palabra)
    
    # Comprobar si el jugador ha adivinado todas las letras   
    if all(letra in adivinado for letra in palabra):
        print("¡Felicidades! ¡Has ganado!")
        break