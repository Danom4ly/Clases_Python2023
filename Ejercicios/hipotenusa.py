import math

c1 = float(input("Ingrese valor del cateto 1 : "))
c2 = float(input("Ingrese valor del cateto 1 : "))
hipo = (c1**2 + c2**2)**(1/2)
#hipo = math.sqrt(c1**2 + c2**2)

print("La hipotenusa es : {}".format(hipo))
