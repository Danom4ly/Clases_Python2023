class Persona:
    def __init__(self, nombre, estado) -> None:
        self._nombre = nombre

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    def movimiento(self, accion):
        print(f"{self.nombre} : {accion}")
