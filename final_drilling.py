
#! Harry Houdini - Newton - David Blaine - Hawking - Messi - Teller - Einstein - Pele - Juanes

##################################################################################################TODO

#? Funciones
#Funcion hacer_grandioso() para modificar la lista de magos
def hacer_grandioso(magos):
    for i in range(len(magos)):
        magos[i] = 'El Gran' + " " + magos[i]

#funcion imprimir_nombres()
def imprimir_nombres(nombres):
    for nombre in nombres:
        print("»",nombre)

#funcion para crear lista
def crear_listas(magos,cientificos,otros,nombres):
    for nombre in nombres:
        if nombre in ['Harry Houdini', 'David Blaine', 'Teller']:
            magos.append(nombre)
        elif nombre in ['Newton', 'Hawking', 'Einstein']:
            cientificos.append(nombre)
        else:
            otros.append(nombre)

#? Variables
# definir lista de nombre
nombres = ['Harry Houdini', 'Newton', 'David Blaine', 'Hawking', 'Messi', 'Teller', 'Einstein', 'Pele', 'Juanes']
magos = []
cientificos = []
otros = []

#? llamando a funciones
crear_listas(magos,cientificos,otros,nombres)
hacer_grandioso(magos)

#? imprimir listas
print("\n---Todos Los Nombres---\n")
imprimir_nombres(nombres)
print("\n---Magos---\n")
imprimir_nombres(magos)
print("\n---Cientificos---\n")
imprimir_nombres(cientificos)
print("\n---Otros---\n")
imprimir_nombres(otros)