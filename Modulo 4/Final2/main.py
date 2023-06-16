from modelo.vehiculo import Vehiculo
from modelo.automovil import Automovil
from service.automovil_service import AutomovilService
from service.menu_service import MenuService


def main():
    #Creando instancias para acceder
    menu_service = MenuService()
    automovil_service = AutomovilService()
    
    while True:
        menu_service.imprimir_menu() #Imprimiendo menu
        opcion = input("Ingrese una opcion: ")
        match opcion:
            case "1":
                automovil_service.automovil_a_insertar("i")
            case "2":
                automovil_service.list_automoviles()
            case "3":
                print("Saliendo del Programa")
                break
            case _:
                print("Opcion invalida")
                
main()