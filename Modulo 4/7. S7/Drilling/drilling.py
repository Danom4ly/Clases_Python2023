class CustomExcpetion(Exception):
    def __init__(self, mensaje) -> None:
        super().__init__(mensaje)

def excepcion_propia():
    try:
        salario = int(input("Ingrese salario para manejar exepciones: "))
        if salario >= 2000 & salario <= 1000:
            raise CustomExcpetion("Salario no esta definido en el rango (1000 a 2000)")
        print(f"El Salario es: {salario}")
    except ValueError:
        print("Error: no permitido")
        
excepcion_propia()