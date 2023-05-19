from trabajador import Trabajador

trabajador1 = Trabajador(
    "Juan", "Perez", "2005", "Ingenieria de software", "IS", "20000"
)

print(trabajador1.nombre)
print(trabajador1.apellido)
print(trabajador1.nombre_dpto)
print(trabajador1.salario)

print(trabajador1.__dict__)