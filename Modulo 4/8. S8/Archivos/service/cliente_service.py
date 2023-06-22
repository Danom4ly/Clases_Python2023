from modelo.cliente import Cliente

class ClienteService:

    #constructor
    def __init__(self):
        #ClienteService tiene una lista de clientes como atributos para que la lista persista en la ejecución
        self._clientes = self.load_clientes()
    
    #Carga de archivo, lectura y creacion si el archivo no existe
    def load_clientes(self):
        try:
            with open("clientes.txt","r") as file:# apertura y cierra el archivo, se puede establecer el tipo de apertura, r es para leer
                clientes = file.readlines() #retorna una lista de tipo str
        except FileNotFoundError:
            with open("clientes.txt","w") as file:
                clientes = []
                file.writelines(clientes) # Escribir el archivo si no existe, w es para escribir
        return clientes

    #Guardado de archivo, escritura sobre el archivo de la lista de clintes
    def save_clientes(self):
        with open('clientes.txt','w') as file:
            for cliente in self._clientes: #se recorre la lista existente de clientes
                file.write(str(cliente)) #se va escribiendo en el archivo cliente a cliente

    def crear_cliente(self):
        #(self, nombre, apellido, rut, area)
        nombre = input("Ingrese nombre del cliente: ")
        apellido = input("Ingrese apellido del cliente: ")
        rut = input("Ingrese rut del cliente: ")
        descuento = input("Ingrese descuento del cliente: ")
        
        #para crear un supervisor se realiza una instancia de su contructor
        cliente = Cliente(nombre, apellido, rut, descuento)
        print("Cliente creado: ", cliente)

        #agregar el cliente a la lista existente en ClienteService
        self._clientes.append(cliente)
        
        #guardar los clientes
        self.save_clientes()
        
    #Metodo para listar los clientes en la lista existente en ClienteService
    def list_clientes(self):
        #retorna la lista de clientes
        print("Lista de clientes")
        for cliente in self._clientes:
            print(cliente)
            
    #metodo para obtener un cliente en la lista existente por Rut
    def get_cliente_by_rut(self, rut):
        for cliente in self._clientes:
            if cliente.rut == rut:
                return cliente
        return None #Si no sucede lo que esta dentro del ciclo for
    
    #metodo para editar el cliente
    def edit_cliente(self, rut):
        rut = input("Ingrese el rut del cliente a editar: ")
        for cliente in self._clientes:
            if cliente.rut == rut:
                print("cliente encontrado: ")
                    