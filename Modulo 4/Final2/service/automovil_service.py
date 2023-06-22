from modelo.automovil import Automovil
import csv

class AutomovilService:
    
    #constructor
    def __init__(self):
        #ClienteService tiene una lista de clientes como atributos para que la lista persista en la ejecución
        self._automoviles = self.load_automoviles("nombre_archivo")
    
    #Carga de archivo, lectura y creacion si el archivo no existe
    def load_automoviles(self, nombre_archivo):
        vehiculos = []
        archivo = open(nombre_archivo, "r")
        archivo_csv = csv.reader(archivo)
        for vehiculo in archivo_csv:
            vehiculos.append(vehiculo)
            archivo.close()
            return vehiculos

    #Guardado de archivo, escritura sobre el archivo de la lista de clintes
    def save_automoviles(self, nombre_archivo, Automovil):
            archivo = open(nombre_archivo, "w")
            datos = [(Automovil.__class__, Automovil.__dict__)]
            archivo_csv = csv.writer(archivo)
            archivo_csv.writerows(datos)
            archivo.close()

    def automovil_a_insertar(self,i):
        ingreso = int(input("Cuantos automoviles desea insertar: "))
        i = 1
        automovil_service = AutomovilService()
        while i <= ingreso:
            automovil_service.crear_automovil(i)
            i += 1

    def crear_automovil(self, i):
        marca = input("Ingrese marca del automovil: ")
        modelo = input("Ingrese modelo del automovil: ")
        numero_ruedas = input("Ingrese numero de ruedas del automovil: ")
        velocidad = input("Ingrese velocidad del automovil: ")
        cilindrada = input("Ingrese cilindrada del automovil: ")
        
        #para crear un supervisor se realiza una instancia de su contructor
        automovil = Automovil(marca, modelo, numero_ruedas, velocidad, cilindrada)
        print(f"Automovil creado: ", automovil)

        #agregar el cliente a la lista existente en ClienteService
        self._automoviles.append(automovil)
        
        #guardar los clientes
        self.save_automoviles()
        
    #Metodo para listar los clientes en la lista existente en ClienteService
    def list_automoviles(self):
        #retorna la lista de clientes
        print("Lista de automoviles")
        for automovil in self._automoviles:
            print(automovil)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # def crear_automovil(self, i):
    #     marca = input("Ingrese marca del automovil: ")
    #     modelo = input("Ingrese modelo del automovil: ")
    #     numero_ruedas = input("Ingrese numero de ruedas del automovil: ")
    #     velocidad = input("Ingrese velocidad del automovil: ")
    #     cilindrada = input("Ingrese cilindrada del automovil: ")

    #     #para crear un supervisor se realiza una instancia de su contructor
    #     automovil = Automovil(marca, modelo, numero_ruedas, velocidad, cilindrada)
    #     lista = []
    #     lista.append(automovil)
    #     print(f"Automovil {i} creado: ", automovil)
