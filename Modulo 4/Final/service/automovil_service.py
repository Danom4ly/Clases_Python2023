from modelo.automovil import Automovil

class AutomovilService:
    
    #constructor
    def __init__(self):
        #ClienteService tiene una lista de clientes como atributos para que la lista persista en la ejecución
        self._automoviles = self.load_automoviles()
    
    #Carga de archivo, lectura y creacion si el archivo no existe
    def load_automoviles(self):
        try:
            with open("automoviles.txt","r") as file:# apertura y cierra el archivo, se puede establecer el tipo de apertura, r es para leer
                automoviles = file.readlines() #retorna una lista de tipo str
        except FileNotFoundError:
            with open("automoviles.txt","w") as file:
                automoviles = []
                file.writelines(automoviles) # Escribir el archivo si no existe, w es para escribir
        return automoviles

    #Guardado de archivo, escritura sobre el archivo de la lista de clintes
    def save_automoviles(self):
        with open('automoviles.txt','w') as file:
            for automovil in self._automoviles: #se recorre la lista existente de clientes
                file.write(str(automovil)) #se va escribiendo en el archivo cliente a cliente

    def crear_automovil(self):
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
