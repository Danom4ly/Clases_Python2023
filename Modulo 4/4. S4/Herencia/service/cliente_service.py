from modelo.cliente import Cliente

class ClienteService:
    def crear_cliente(self):
        #(self, nombre, apellido, rut, area)
        nombre = input("Ingrese nombre del cliente: ")
        apellido = input("Ingrese apellido del cliente: ")
        rut = input("Ingrese rut del cliente: ")
        descuento = input("Ingrese descuento del cliente: ")
        
        #para crear un supervisor se realiza una instancia de su contructor
        cliente = Cliente(nombre, apellido, rut, descuento)
        print("Cliente creado: ", cliente)