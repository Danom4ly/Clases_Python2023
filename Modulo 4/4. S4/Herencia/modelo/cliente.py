from modelo.persona import Persona

class Cliente(Persona):
    def __init__(self, nombre, apellido, rut, descuento):
        super().__init__(nombre,apellido,rut)#invocando a los atributos de la super clase persona
        self._descuento = descuento
        
    @property
    def descuento(self):
        return self._descuento
    
    @descuento.setter
    def descuento(self, descuento):
        self._descuento = descuento
        
    def __str__(self):
        return f"Cliente(Nombre: {self.nombre}, Apellido: {self.apellido}, Rut: {self.rut}, Descuento: {self.descuento})"