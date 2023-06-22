class vehiculo:
    #constructor con parametros para realizar una instancia de la clase vehiculo
    def __init__(self, marca, color, modelo, peso, ancho, alto):
        self.marca = marca
        self.color = color
        self.modelo = modelo
        self.peso = peso
        self.ancho = ancho
        self.alto = alto
    
    #constructor sin parametros de entrada para instanciar un objeto vehiculo
    def __init__(self, marca=None, color=None, modelo=None, peso=None, ancho=None, alto=None):
        self.marca = marca
        self.color = color
        self.modelo = modelo
        self.peso = peso
        self.ancho = ancho
        self.alto = alto


#metodo para imprimir la informacion de una instancia de la clase vehiculo
def imprimir_vehiculo_uno():
    print("Marca: ", vehiculo_uno.marca)
    print("Color: ", vehiculo_uno.color)
    print("Modelo: ", vehiculo_uno.modelo)
    print("Peso: ", vehiculo_uno.peso)
    print("Ancho: ", vehiculo_uno.ancho)
    print("Alto: ", vehiculo_uno.alto)

def imprimir_vehiculo_tres():
    print("Marca: ", vehiculo_tres.marca)
    print("Color: ", vehiculo_tres.color)
    print("Modelo: ", vehiculo_tres.modelo)
    print("Peso: ", vehiculo_tres.peso)
    print("Ancho: ", vehiculo_tres.ancho)
    print("Alto: ", vehiculo_tres.alto)

#creando una instancia de la clase vehiculo
vehiculo_uno = vehiculo("Mazda","blanco","M3",2000,2.5,2.0)
vehiculo_dos = vehiculo("BWM","Gris","M4",800,2,1.5)
vehiculo_tres = vehiculo()

#Cambiar los valores de los atributos del objeto llamado vehiculo_uno
vehiculo_uno.marca = "Toyota"
vehiculo_uno.color = "Negro"
vehiculo_uno.modelo = "Camry"
vehiculo_uno.peso = 1000
vehiculo_uno.ancho = 2.0
vehiculo_uno.alto = 1.5

#Asignar valores al objeto vehiculo llamadao vehiculo_tres

vehiculo_tres.marca = "VW"
vehiculo_tres.color = "Rosado"
vehiculo_tres.modelo = "Escarabajo"
vehiculo_tres.peso = 600
vehiculo_tres.ancho = 1.5
vehiculo_tres.alto = 1.5


#imprimiendo valores
imprimir_vehiculo_uno()
imprimir_vehiculo_tres()