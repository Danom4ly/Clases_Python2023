from modelo.vehiculo import Vehiculo

#Clase automovil
class Automovil(Vehiculo): #Herencia con Vehiculo
    #Constructor
    def __init__(self, marca, modelo, numero_ruedas, velocidad, cilindrada) -> None:
        super().__init__(marca, modelo, numero_ruedas)
        #atributos del objeto automovil
        self._velocidad = velocidad
        self._cilindrada = cilindrada

    @property
    def velocidad(self):
        return self._velocidad
    @velocidad.setter
    def velocidad(self, velocidad):
        return self._velocidad
    
    @property
    def cilindrada(self):
        return self._cilindrada
    @cilindrada.setter
    def cilindrada(self, cilindrada):
        return self._cilindrada
    
    #Método toString
    def __str__(self):
        return f"{self.marca} {self.modelo} - {self.numero_ruedas} - Velocidad: {self.velocidad} - Cilindrada: {self.cilindrada}"