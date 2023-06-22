from persona import Persona
from departamento import Departamento

class Trabajador(Persona, Departamento):
    def __init__(self,nombre,apellido,anio,nombre_dpto,nombre_corto_dpto,salario) -> None:
        Persona.__init__(self,nombre,apellido,anio)
        Departamento.__init__(self,nombre_dpto,nombre_corto_dpto)
        self._salario = salario

    @property
    def salario(self):
        return self._salario
    
    @salario.setter
    def salario(self, salario):
        self._salario = salario
        
    def __str__(self):
        return f'Trabajador(nombre={self._nombre}, apellido={self._apellido}, anio={self._anio}, nombre_dpto={self._nombre_dpto}, nombre_corto_dpto={self._nombre_corto}, salario={self._salario})'

