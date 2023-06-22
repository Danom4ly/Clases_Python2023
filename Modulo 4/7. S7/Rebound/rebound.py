while True:
    try:
        edad = int(input("Ingrese su edad: "))
        if edad >= 18:
            print("Es mayor de edad")
        else:
            print("Es menor de edad")
        break
    except ValueError:
        print("Error: Cararcter invalido, favor ingrese un numero entero")
