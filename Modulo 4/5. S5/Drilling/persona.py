class Persona: # Constructor con parametros
    def __init__(self, nombre, apellido, anio) -> None:
        self._nombre = nombre
        self._apellido = apellido
        self._anio = anio
        
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
    
    @property
    def apellido(self):
        return self._apellido
    
    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido
        
    @property
    def anio(self):
        return self._anio
    
    @anio.setter
    def anio(self, anio):
        self._anio = anio
        
    def __str__(self):
        return f'Persona(nombre={self._nombre}, apellido={self._apellido}, anio={self._anio})'