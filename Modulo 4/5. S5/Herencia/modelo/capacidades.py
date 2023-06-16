<<<<<<< HEAD
class Capacidades:
    def __init__(self, ncertificados, rating) -> None:
        self._ncertificados = ncertificados
        self._rating = rating
        
    @property
    def ncertificados(self):
        return self._ncertificados
    
    @ncertificados.setter
    def ncertificados(self,ncertificados):
        self._ncertificados = ncertificados

    @property
    def rating(self):
        return self._rating
    
    @rating.setter
    def rating(self,rating):
        self._rating = rating
        
    def __str__(self) -> str:
=======
class Capacidades:
    def __init__(self, ncertificados, rating) -> None:
        self._ncertificados = ncertificados
        self._rating = rating
        
    @property
    def ncertificados(self):
        return self._ncertificados
    
    @ncertificados.setter
    def ncertificados(self,ncertificados):
        self._ncertificados = ncertificados

    @property
    def rating(self):
        return self._rating
    
    @rating.setter
    def rating(self,rating):
        self._rating = rating
        
    def __str__(self) -> str:
>>>>>>> 2d9caed6ea9dd162443604ddc951806c7468a871
        return f'Capacidades(ncertificados={self.ncertificados}, rating={self.rating})' 