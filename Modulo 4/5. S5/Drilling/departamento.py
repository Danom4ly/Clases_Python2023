class Departamento:
    def __init__(self, nombre_dpto, nombre_corto_dpto) -> None:
        self._nombre_dpto = nombre_dpto
        self._nombre_corto_dpto = nombre_corto_dpto
        
    @property
    def nombre_dpto(self):
        return self._nombre_dpto
    
    @nombre_dpto.setter
    def nombre_dpto(self, nombre_dpto):
        self._nombre_dpto = nombre_dpto
        
    @property
    def nombre_corto_dpto(self):
        return self._nombre_corto_dpto
    
    @nombre_corto_dpto.setter
    def nombre_corto_dpto(self, nombre_corto_dpto):
        self._nombre_corto_dpto = nombre_corto_dpto
        
    def __str__(self):
        return f'Departamento(nombre_dpto={self._nombre_dpto}, nombre_corto_dpto={self._nombre_corto_dpto})'