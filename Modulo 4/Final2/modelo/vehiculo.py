#Clase Vehiculo
class Vehiculo:
    #Constructor
    def __init__(self, marca, modelo, numero_ruedas) -> None:
        #Atributos del obejto Vehiculo
        self._marca = marca
        self._modelo = modelo
        self._numero_ruedas = numero_ruedas
        
    @property 
    def marca(self):
        return self._marca
    @marca.setter
    def marca(self, marca):
        self._marca = marca
    
    @property
    def modelo(self):
        return self._modelo
    @modelo.setter
    def modelo(self, modelo):
        self._modelo = modelo
    
    @property
    def numero_ruedas(self):
        return self._numero_ruedas
    @numero_ruedas.setter
    def numero_ruedas(self, numero_ruedas):
        self._numero_ruedas = numero_ruedas
    
    #Método toString
    def __str__(self):
        return f"Marca: {self._marca} \nModelo: {self._modelo} \nRuedas: {self._numero_ruedas}"
