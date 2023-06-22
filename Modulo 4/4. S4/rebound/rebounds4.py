class Libro:
    def __init__(self, autor=None, titulo=None, anno_de_publicacion=None):
        self.autor = autor
        self.titulo = titulo
        self.anio_de_publicacion = anno_de_publicacion
    
    @property
    def autor(self):
        return self._autor
    
    @autor.setter
    def autor(self, autor):
        self._autor = autor
        
    @property
    def titulo(self):
        return self._titulo
    
    @titulo.setter
    def titulo(self, titulo):
        self._titulo = titulo
        
    @property
    def anio_de_publicacion(self):
        return self._anio_de_publicacion
    
    @anio_de_publicacion.setter
    def anio_de_publicacion(self, anio_de_publicacion):
        self._anio_de_publicacion = anio_de_publicacion
        
    def __str__(self) -> str:
        return f"Autor: {self._autor}\nTitulo: {self._titulo}\nAnio de Publicacion: {self._anio_de_publicacion}"


libro_1 = Libro('Dan Brown','Infierno')

libro_2 = Libro('Dan Brown','El Codigo Da Vinci','2003')

print("---------------------------------")
print(libro_1.__dict__)
print("---------------------------------")
print(libro_2.__dict__)
print("---------------------------------")
libro_1.anio_de_publicacion = "2013"
print(libro_1.__dict__)
print("---------------------------------")
print(libro_1)
print("---------------------------------")
print(libro_2)
print("---------------------------------")
print(libro_1.__str__)
print(libro_2.__str__)
print("---------------------------------")