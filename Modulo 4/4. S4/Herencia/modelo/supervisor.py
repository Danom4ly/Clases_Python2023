from modelo.persona import Persona

class Supervisor(Persona):
    def __init__(self, nombre, apellido, rut, area):
        super().__init__(nombre, apellido, rut)#atributos de la super clasee
        self._area = area
        
    @property #get()
    def area(self):
        return self._area
    
    @area.setter #set()
    def area(self, area):
        self._area = area
        
    def __str__(self):
        #return super().__str__()
        return f"Supervisor(nombre={self.nombre}, apellido={self.apellido}, rut={self.rut}, area={self.area}"
    