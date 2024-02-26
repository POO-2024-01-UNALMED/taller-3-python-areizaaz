from tv import TV

class Control:

    def __init__(self) -> None:
         TV._tv = None

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