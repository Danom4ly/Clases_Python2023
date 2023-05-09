"""
Se solicita crear un programa en Python que permita llevar el registro de los invitados
a una fiesta.
"""


def agregar_invitados_confirmados():
    set_confirmados = set()
    print("Cuantos invitados confirmados desea ingresar")
    confirmados = int(input("ingrese la cantidad: "))
    for i in range(confirmados):
        set_confirmados.add(input(f"Nombre del {i+1}er invitado: "))
    return set_confirmados

def agregar_invitados_asistentes(set_asistentes):
    print("Ingrese el nombre del invitado: ", end="")
    set_asistentes.add(input())
    return set_asistentes

def cantidad_confirmados_o_asistentes(datos,):
    print("La cantidad es: ", len(datos))

def conocer_faltantes(invitados_confirmados,invitados_asistentes):
    faltantes = invitados_confirmados - invitados_asistentes
    print(f"Los invitados que no asistieron son: {faltantes}")











""" 
#!crear dos conjuntos (set): uno con los nombres de los invitados confirmados y otro con los nombres de los invitados que han llegado a la fiesta.
#?Creacion de variables en set
invitados_confirmados = {"Maria","Fulanito","Jose","Cleopatra","Mario","Feliciano"}
invitados_que_asistieron = set()

#!A medida que los invitados van llegando a la fiesta, se deben ir agregando sus nombres al conjunto de los que asistieron.
#?invitados que asistieron
invitados_que_asistieron.add("Maria")
invitados_que_asistieron.add("Cleopatra")
invitados_que_asistieron.add("Feliciano")
invitados_que_asistieron.add("Jose")
invitados_que_asistieron.add("Fulanito")
invitados_que_asistieron.add("Mario")

#!imprimir en pantalla la cantidad de invitados confirmados y la cantidad de invitados que han asistido.
#?Imprimiendo invitados confirmados y los que asistieron
print(f"Invitados confirmados", len(invitados_confirmados))
print(f"Invitados que asistieron", len(invitados_que_asistieron))

#!Finalmente, se debe imprimir en pantalla el nombre de los invitados que confirmaron su asistencia pero aún no han llegado a la fiesta, es decir, 
#!los nombres que se encuentran en el conjunto de confirmados pero no en el conjunto de los que asistieron.
#?invitados que no asistieron
#invitados_faltantes = invitados_confirmados - invitados_que_asistieron
#invitados_faltantes = invitados_confirmados.difference(invitados_que_asistieron)
#invitados_faltantes = invitados_confirmados.symmetric_difference(invitados_que_asistieron)
invitados_faltantes = invitados_confirmados.difference(invitados_que_asistieron)

print(f"Invitados que no asistieron", (invitados_faltantes))
"""