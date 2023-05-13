from modelo.supervisor import Supervisor

class SupervisorService:
    def crear_supervisor(self):
        #(self, nombre, apellido, rut, area)
        nombre = input("Ingrese nombre del supervisor: ")
        apellido = input("Ingrese apellido del supervisor: ")
        rut = input("Ingrese rut del supervisor: ")
        area = input("Ingrese area del supervisor: ")
        
        #para crear un supervisor se realiza una instancia de su contructor
        supervisor = Supervisor(nombre, apellido, rut, area)
        print("Supervisor creado: ", supervisor)