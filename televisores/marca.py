class Marca:
    def __init__(self, nombre) -> None:
        self._nombre = nombre
    
    def setNombre(self,nom):
        self._nombre = nom
    
    def getNombre(self):
        return self._nombre

class TV:
    _numTV = 0
    def __init__(self, marca, estado) -> None:
        self._marca = marca
        self._canal = int(1)
        self._precio = int(500)
        self._estado = estado
        self._volumen = int(1)
        self._control = None

        TV._numTV += 1

    def setMarca(self,marca):
        self._marca = marca
    def setCanal(self,canal):
        self._canal = canal
    def setPrecio(self,precio):
        self._precio = precio
    def setVolumen(self,volumen):
        self._volumen = volumen
    def setControl(self,control):
        self._control = control

    def getMarca(self):
        return self._marca
    def getCanal(self):
        return self._marca
    def getPrecio(self):
        return self._precio
    def getVolumen(self):
        return self._volumen
    def getControl(self):
        return self._control

    @classmethod
    def setNumTV(cls,numero):
        cls._numTV = numero
    
    @classmethod
    def getNumTV(cls):
        return cls._numTV

    def turnOn(self,estado):
        self._estado = estado
    def turnOff(self,estado):
        self._estado = estado
    
    def getEstado(self):
        return self._estado

    def canalUp(self):
        if(self._estado and self._canal < 120):
            self._canal += 1
    def canalDown(self):
        if(self._estado and self._canal > 1):
            self._canal -= 1
    
    def volumenUp(self):
        if(self._estado and self._volumen < 7):
            self._volumen += 1
    def volumenDown(self):
        if(self._estado and self._volumen > 0):
            self._volumen -= 1
    
class Control:

    def __init__(self) -> None:
         self._tv = None

    def turnOn(self):
        TV.turnOn()
    def turnOff(self):
        TV.turnOff()
    def canalUp(self):
        TV.canalUp()
    def canalDown(self):
        TV.canalDown()
    def volumenUp(self):
        TV.volumenUp()
    def volumenDown(self):
        TV.volumenDown()

    def enlazar(self,tv):
        self._tv = tv
        TV._control = self.tv

    def setCanal(self, canal):
        if(canal >= 1 and canal <= 120):
            self._canal = canal
    def setVolumen(self, volumen):
        if(volumen >= 0 and volumen <= 7):
            self._volumen = volumen
    
    def setTv(self,tv):
        self._tv = tv
    def getTv(self):
        return self._tv
