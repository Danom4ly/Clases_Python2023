<<<<<<< HEAD
from modelo.supervisor import Supervisor
from modelo.capacidades import Capacidades

class SupervisorZona(Supervisor,Capacidades):
    def __init__(self, nombre, apellido, rut, area, ncertificados, rating, promedio):
        Supervisor.__init__(self,nombre, apellido, rut, area)
        Capacidades.__init__(self,ncertificados, rating)
        self._promedio = promedio
        
    @property
    def promedio(self):
        return self._promedio
        
    @promedio.setter
    def promedio(self, promedio):
=======
from modelo.supervisor import Supervisor
from modelo.capacidades import Capacidades

class SupervisorZona(Supervisor,Capacidades):
    def __init__(self, nombre, apellido, rut, area, ncertificados, rating, promedio):
        Supervisor.__init__(self,nombre, apellido, rut, area)
        Capacidades.__init__(self,ncertificados, rating)
        self._promedio = promedio
        
    @property
    def promedio(self):
        return self._promedio
        
    @promedio.setter
    def promedio(self, promedio):
>>>>>>> 2d9caed6ea9dd162443604ddc951806c7468a871
        self._promedio = promedio