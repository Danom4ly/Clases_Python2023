from persona import Persona
from departamento import Departamento
from trabajador import Trabajador

def conocer_instancia(objeto, objeto_comparar):
    return 'Si' if isinstance(objeto, objeto_comparar) else 'No'

trabajador1 = Trabajador("Juan", "Perez", "2005", "Ingenieria de software", "IS", "20000")

# print(trabajador1.nombre)
# print(trabajador1.apellido)
# print(trabajador1.nombre_dpto)
# print(trabajador1.salario)

#! Drilling

print(trabajador1.__dict__)
print("Es trabajador instancia de Persona: ",conocer_instancia(trabajador1, Persona))
print("Es trabajador instancia de Departamento: ",conocer_instancia(trabajador1, Departamento))
print("Es trabajador instancia de Trabajador: ",conocer_instancia(trabajador1, Trabajador))

