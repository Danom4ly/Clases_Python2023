from multipledispatch import dispatch

class Animal:
    # def __init__(self, nombre:str, raza:str, edad:int, peso:float):
    #     self.nombre = nombre
    #     self.raza = raza
    #     self.edad = edad
    #     self.peso = peso

    # def __init__(self, nombre=None, raza=None, edad=None, peso=None):
    #     self.nombre = nombre
    #     self.raza = raza
    #     self.edad = edad
    #     self.peso = peso

    # Usando multipledispatch para generar y estructurar el tipo de dato insterto en la instancia
    @dispatch(str, str, int, float)
    def __init__(self, nombre, raza, edad, peso):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.peso = peso

    #! GET

    def get_nombre(self):
        return self.nombre

    def get_raza(self):
        return self.raza

    def get_edad(self):
        return self.edad

    def get_peso(self):
        return self.peso

    #! SET

    def set_nombre(self,nombre):
        self.nombre = nombre

    def set_raza(self,raza):
        self.raza = raza

    def set_edad(self,edad):
        self.edad = edad

    def set_peso(self,peso):
        self.peso = peso

caballo = Animal("Zeus","Pura Sangre",5,450.0)
leon = Animal("Boulder","Atlas",10,130.0)

print(caballo.get_nombre())
print(caballo.get_raza())
print(caballo.get_edad())
print(caballo.get_peso())
print("----------------------------")
print(leon.get_nombre())
print(leon.get_raza())
print(leon.get_edad())
print(leon.get_peso())

caballo.set_raza("Potrillo")
print(caballo.get_raza())