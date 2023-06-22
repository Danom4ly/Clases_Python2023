
#? Las excepciones pueden ocurrir en el momento de transformacion, asignacion, evaluacion de variables o atributos 
#? Las execpciones ocurren con errores de ejecución
#? Comunicando con entes externos al proyecto


""" # Error aritmetico
try:
    num1 = 10 
    num2 = 0
    division = num1 / num2
    print(division)
    
except ZeroDivisionError as e:
    print(f'Error: {e} no permitido') """
    
# input invalido, transformacion de datos
""" try:
    ingreso = int(input("ingrese un número: "))
    print(f"El numero ingresado es: {ingreso}")
except ValueError as e:
    print(f'Error: {e} no permitido') #Error: invalid literal for int() with base 10: 's' no permitido """
"""     
def ingreso():
    try:
        ingreso = int(input("ingrese un número: "))
        print(f"El numero ingresado es: {ingreso}")
    except ValueError as e:
        print(f'Error: {e} no permitido') #Error: invalid literal for int() with base 10: 's' no permitido 
        
def division_ingreso():
    try:
        num1 = int(input("ingrese primer número: "))
        num2 = int(input("ingrese segundo número: "))
        
        division = num1 / num2
        print(division)
        
    except Exception as e:
        print(f'Error: {e} no permitido')
        division_ingreso()
        
division_ingreso() """

#crear excepcion propia, para ciertos casos
class CustomExcpetion(Exception):
    def __init__(self, mensaje, codigo) -> None:
        super().__init__(mensaje)
        self.codigo = codigo

def excepcion_propia():
    try:
        edad = int(input("Ingrese edad para manejar exepciones: "))
        if edad < 0:
            raise CustomExcpetion("Excepcion propia ejecutada", 460)
        print(f"La edad es: {edad}")
    except ValueError:
        print("Error: no permitido")
    except CustomExcpetion as e:
        print(f"Error: {e} y manejada")
        print(f"Codigo: {e.codigo}")
        
excepcion_propia()