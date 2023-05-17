class A:
    def __init__(self):
        print("Pertenezco a la clase A")
    def metodo_a(self):
        print("Metodo heredado de A")
        
class B:
    def __init__(self):
        print("Clase B")
    def metodo_b(self):
        print("Metodo heredado de B")
        
class C(B,A):
    def metodo_c(self):
        print("Metodo de clase C")
        
c = C()
c.metodo_a()
c.metodo_b()
c.metodo_c()
