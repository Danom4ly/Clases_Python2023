""" Realizar la ejecución de un menú utilizando el lenguaje Python, donde se
le indiquen varias opciones a seleccionar por el usuario y una opción para
salir del menú.
Utilizar ciclos y estructuras condicionales. """

#importar libreria para exprtesiones regulares

#varias opciones a seleccionar

opcion = ""

while opcion != "5":
    print("Hola, bienvenido al menú")
    print("1. Opcion 1")
    print("2. Opcion 2")
    print("3. Opcion 3")
    print("4. Opcion 4")
    print("5. Salir del menú")
    print("Ingrese una opción")

    opcion = input() #leyendo la opción

    if opcion == "1":
        print("Opcion 1")
    elif opcion == "2":
        print("Opcion 2")
    elif opcion == "3":
        print("Opcion 3")
    elif opcion == "4":
        print("Opcion 4")
    elif opcion == "5":
        print("Saliendo del menú")
    else :
        print("Ha ingresado una opción invalida, por favor ingrese una opción")

