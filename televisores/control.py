class Control:

    
    #def __init__(tv):
    #   _tv = tv

    def turnOn(self):
        self._tv.turnOn(self._tv)
    def turnOff(self):
        self._tv.turnOff(self._tv)
    def canalUp(self):
        self._tv.canalUp(self._tv)
    def canalDown(self):
        self._tv.canalDown(self._tv)
    def volumenUp(self):
        self._tv.volumenUp(self._tv)
    def volumenDown(self):
        self._tv.volumenDown(self._tv)

    def enlazar(self, tv):
        self._tv = tv
        tv.setControl(self)

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