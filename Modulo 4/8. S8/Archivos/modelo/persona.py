class Persona:
    #constructor con parametros para instanciar un objeto de tipo persona
    def __init__(self, nombre, apellido, rut):
        self._nombre = nombre
        self._apellido = apellido
        self._rut = rut
        
    #!getters y setters
    @property #get() objeto.nombre
    def nombre(self):
        return self._nombre
    
    @nombre.setter #set() objeto.nombre
    def nombre(self, nombre):
        self._nombre = nombre
        
    @property #get() objeto.apellido
    def apellido(self):
        return self._apellido
    
    @apellido.setter #set() objeto.apellido
    def apellido(self, apellido):
        self._apellido = apellido
        
    @property #get() objeto.rut
    def rut(self):
        return self._rut
    
    @rut.setter #set() objeto.rut
    def rut(self, rut):
        self._rut = rut

    #funcion o metodos
    def get_tipo(self):
        print(f'Soy del tipo {self}')
        print(type(self))
    
    #function para imprimir el objeto en string
    def __str__(self):
        return f'Persona(nombre={self._nombre}, apellido={self._apellido}, rut={self._rut})'