class Persona:
    def __init__(self, nombre, apellidos, sexo, edad, estatura, peso):
        self._nombre = nombre
        self._apellidos = apellidos
        self._sexo = sexo
        self._edad = edad
        self._estatura = estatura
        self._peso = peso

    # Getter y Setter

    @property  # get permite acceder al valor
    def nombre(self):
        return self._nombre

    @nombre.setter  # set permite setear un nuevo valor
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def apellidos(self):
        return self._apellidos

    @apellidos.setter
    def apellidos(self, apellidos):
        self._apellidos = apellidos

    @property
    def sexo(self):
        return self._sexo

    @sexo.setter
    def sexo(self, sexo):
        self._sexo = sexo

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad

    @property
    def estatura(self):
        return self._estatura

    @estatura.setter
    def estatura(self, estatura):
        self._estatura = estatura

    @property
    def peso(self):
        return self._peso

    @peso.setter
    def peso(self, peso):
        self._peso = peso

    def __str__(self):
        return f'Persona(nombre= {self.nombre}, apellidos= {self.apellidos}, sexo= {self.sexo}, edad= {self.edad}, estatura= {self.estatura}, peso= {self.peso})'

#Asignando Valores
persona_1 = Persona("Pedro", "Vivas", "Masculino", "20 años", "1.78 mts", "68 Kg.")
persona_2 = Persona("Juan", "Camargo", "Masculino", "18 años", "1.8 mts", "75 Kg.")


print("---------------------------")
print(persona_1) #imprimiendo persona a traves del metodo definido por __str__
print(persona_2) #imprimiendo persona a traves del metodo definido por __str__
print("ANTES")
print(f"La edad de {persona_1.nombre} es {persona_1.edad}.") #accediendo a traves de get
print(f"El nombre de persona 1 es {persona_2.nombre} y su apellido es {persona_2.apellidos}.") #accediendo a traves de get

#!DRILLING
persona_1.edad = "21 años" # Seteando un nuevo valor a traves de setter
persona_2.apellidos = "Santiago" # Seteando un nuevo valor a traves de setter

print("---------------------------")
print(persona_1) #imprimiendo persona a traves del metodo definido por __str__
print(persona_2) #imprimiendo persona a traves del metodo definido por __str__
print("DESPUES")
print(f"La edad de {persona_1.nombre} es {persona_1.edad}.") #accediendo a traves de get
print(f"El nombre de persona 1 es {persona_2.nombre} y su apellido es {persona_2.apellidos}.") #accediendo a traves de get