class Paciente:

    PREVISIONES: set[str] = {"Fonasa","Isapre"}
    def __init__(self, rut:str, nombre:str, edad:int, prevision:str):
        self.rut = rut
        self.edad = edad
        self.nombre = nombre
        self.prevision = prevision

    @property
    def rut(self) -> str:
        return self._rut

    @rut.setter
    def rut(self,rut:str)-> None:
        self._rut = rut

    @property 
    def nombre(self)-> str:
        return self._nombre

    @nombre.setter
    def nombre(self, nombre:str)-> None:
        self._nombre = nombre

    @property 
    def edad(self)-> int:
        return self._edad

    @edad.setter
    def edad(self, edad:int)-> None:
        self._edad = edad

    @property 
    def prevision(self)->str:
        return self._prevision

    @prevision.setter
    def prevision(self, prevision:str)-> None:
        self._prevision = prevision

    def __str__(self)->str:
        return f"Información del Paciente:\nRUT: {self.rut}\nNOMBRE: {self.nombre}\nEDAD: {self.edad}\nPREVISION: {self.prevision}"

    def __repr__(self)->str:
        return f"Paciente(rut='{self.rut}', nombre='{self.nombre}', edad={self.edad}, prevision='{self.prevision}'"
