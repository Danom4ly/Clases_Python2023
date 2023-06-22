""" solicita a1 usuario ingresar una contraseña hasta que la contraseña
ingresada coincida con una contraseña predefinida """

contraseña = "secreta123"
while True:
    ingreso = input("lngrese la contraseña: ")
    if ingreso == contraseña:
        print(" ¡Contraseña correcta!")
        break
    else:
        print("Contraseña incorrecta. Vuelva a intentarlo. ")