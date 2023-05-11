class Vehiculo:
    #constructor con parametros para realizar una instancia de la clase vehiculo
    def __init__(self, marca, color, modelo, peso, ancho, alto):
        self.marca = marca
        self.color = color
        self.modelo = modelo
        self.peso = peso
        self.ancho = ancho
        self.alto = alto
        self.velocidad = 0
        self.marcha = False

    #getters and setters son funciones para obtener o dar valor a los atributos
    #!getters
    def get_marca(self):
        return self.marca
    
    def get_color(self):
        return self.color
    
    def get_modelo(self):
        return self.modelo
    
    def get_peso(self):
        return self.peso
    
    def get_ancho(self):
        return self.ancho
    
    def get_alto(self):
        return self.alto
    
    def get_velocidad(self):
        return self.velocidad
    
    def get_marcha(self):
        return self.marcha

    #!setter
    def set_marca(self,marca):
        self.marca = marca
    
    def set_color(self,color):
        self.color = color
    
    def set_modelo(self,modelo):
        self.modelo = modelo
        
    def set_peso(self,peso):
        self.peso = peso
    
    def set_ancho(self,ancho):
        self.ancho = ancho
        
    def set_alto(self,alto):
        self.alto = alto
        
    def set_velocidad(self,velocidad):
        self.velocidad = velocidad
    
    def set_marcha(self,marcha):
        self.marcha = marcha


    #Funciones que realiza el objeto accediendo a traves de la instancia
    def arrancar(self):
        if not self.marcha:
            self.marcha = True #Se cambia a True para cambiar el estado del vehiculo
            self.velocidad = 10 #Se cambiar el estado del vehiculo
            print(f"Vehiculo de marca {self.marca} esta en marcha a una velocidad de {self.velocidad}")
        else:
            print(f"Vehiculo de marca {self.marca} ya se encuentra en marcha, no se puede volver a arrancar")

    def frenar(self):
        if self.marcha and self.velocidad > 0:
            self.velocidad -= 10
            print(f"Vehiculo de marca {self.marca} esta frenando a una velocidad de {self.velocidad}")
        else:
            print(f"Vehiculo de marca {self.marca} modelo {self.modelo} ya esta detenido")
    
    def girar_izquierda(self,direccion):
        if self.marcha:
            return f"Vehiculo de marca {self.marca} esta girando a la izquierda"
        else:
            return f"Vehiculo de marca {self.marca} debe estar en marcha"    
        
    def girar_derecha(self,direccion):
        if self.marcha:
            return f"Vehiculo de marca {self.marca} esta girando a la derecha "
        else:
            return f"Vehiculo de marca {self.marca} debe estar en marcha"   
        
    def apagar(self):
        if self.marcha:
            self.marcha = False
            return f"Vehiculo de marca {self.marca} se ha apagado"
        else:
            return f"Vehiculo de marca {self.marca} ya se encuentra apagado"
        
    def encender(self):
        if not self.marcha:
            self.marcha = True
            return f"Vehiculo de marca {self.marca} se ha encendido"
        else:
            return f"Vehiculo de marca {self.marca} ya se encuentra encendido"
        
    def acelerar(self):
        if self.marcha:
            self.velocidad += 10
            return f"Vehiculo de marca {self.marca} esta aumentando su velocidad en 10 a una velocidad actual de {self.velocidad}"
        else:
            return f"Vehiculo de marca {self.marca} no se puede acelerar ya que no se encuentra encendido"

    def retroceder(self):
        if self.marcha:
            self.velocidad -= 10
            return f"Vehiculo de marca {self.marca} esta retrocediendo su velocidad en 10 a una velocidad actual de {self.velocidad}"
        else:
            return f"Vehiculo de marca {self.marca} no se puede retroceder ya que no se encuentra encendido"
        
#instanciar vehiculos para realizar las acciones mediante sus funciones o metodos
mazda = Vehiculo("Mazda","Blanco","M4",2000,2.5,2)
toyota = Vehiculo("Toyota","Negro","Yaris",1500,1.5,1)

#cambiar el comportamiento meidante las funciones, accediendo desde la instancia a la funciones
print(mazda.arrancar())
print(mazda.acelerar())
print(mazda.encender())
print(mazda.apagar())
print("----------------------")
print(toyota.encender())
print(toyota.encender())
print(toyota.arrancar())
print(toyota.acelerar())
print(toyota.frenar())

#get obtener el valor del atributo a traves de notacion de puntos
print(mazda.color)
print(mazda.get_color())

#setear (cambiar) valor del atributo a traves de notacion de puntos
mazda.color = "Azul"
mazda.set_color("Rosado")
print(mazda.get_color())
print(mazda.color)

#instancia.set() instancia.get()
toyota.set_modelo("Corolla")
print(toyota.get_color())