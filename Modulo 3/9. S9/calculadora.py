"""
Se pide realizar una calculadora declarando funciones para cada tipo de calculo que se realice
realizar un menu con opciones para seleccionar que calculo se desea realizar
el ingreso es por consola, requerir al usuario la opcion y numeros al que se realizara el calculo
verificar errores de ingreso
verificar division por cero
"""

#def nombre_funcion(parametros):
def suma(num1,num2):
    return num1+num2

def resta(num1,num2):
    return num1-num2

def multiplicacion(num1,num2):
    return num1*num2

def division(num1,num2):
    if num2 == 0:
        return None
    else:
        return num1/num2

def opciones_a_mostrar():
    print("Bienvenido a la Calculadora")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. Division")
    print("5. Salir")
    print("Ingrese una Opcion: ")
    
def ingreso(texto) :
    num = float(input(texto))
    return num

#funcion calculadora, llevará el menu y realizará los calculos usando las funciones y estructuras condicionales
def calculadora():

    while True: #mientras sea True o no exista un break o return, se seguira ejecutando el ciclo
        try:
            #Requerir y mostrar opciones al usuario
            opciones_a_mostrar()
            
            #ingresar los valores de opcion
            opcion_a_seleccionar = input("1/2/3/4/5: ")
            #num1 = float(input("Ingrese primer valor: "))
            #num2 = float(input("Ingrese segundo valor: "))
            
            #evaluar opcion y seleccionar una funcion a realizar si se cumple la condición
            match opcion_a_seleccionar:
                case "1": 
                    resultado = suma(ingreso("Ingrese primer valor: "),ingreso("Ingrese segundo valor: ")) #invocando a la funcion suma, que necesita dos parametros de ingreso
                case "2":
                    resultado = resta(ingreso("Ingrese primer valor: "),ingreso("Ingrese segundo valor: "))
                case "3":
                    resultado = multiplicacion(ingreso("Ingrese primer valor: "),ingreso("Ingrese segundo valor: "))
                case "4":
                    resultado = division(ingreso("Ingrese primer valor: "),ingreso("Ingrese segundo valor: "))
                case "5":
                    #return si es funcion
                    #break si es ciclo
                    print ("Gracias por usar la calculadora vuelva pronto!!!")
                    break
                case _:
                    #resultado = None
                    print("Opción no valida")
                    
            if resultado is not None:
                print("El resultado es: ",resultado)
            else:
                print("No se pudo realizar el calculo")
                    
        except Exception as e: #si sucede algun error, se imprime en consola el error
            print("Error: ",e)
            



calculadora() #invocando a la funcion calculadora