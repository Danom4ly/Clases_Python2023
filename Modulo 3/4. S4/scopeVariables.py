#scope o alcance de una variable

#alcance global
#alcance local

#variable de alcance global porque no esta dentro de alguna estructura
variable_goblal = "se puede acceder desde todo el documento"


#metodo o funcion para ejemplicar una variable local
#def nombre_metodo(parametros_entrada):
def suma(a,b):
    suma_valores = a+b #variable local porque existe solo dentro de la estructura de la funcion o metodo
    return suma_valores

print(suma(2,1)) #3
print(variable_goblal)
#print(suma_valores)

