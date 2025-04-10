class Nodo:
    def __init__(self, dato):
        self._dato_ = dato
        self._hijoIzquierdo_ = None
        self._hijoDerecho_ = None

    def getDato(self):
        return self._dato_

    def setDato(self, dato):
        self._dato_ = dato

    def getHijoIzquierdo(self):
        return self._hijoIzquierdo_

    def setHijoIzquierdo(self, hijoIzquierdo):
        self._hijoIzquierdo_ = hijoIzquierdo

    def getHijoDerecho(self):
        return self._hijoDerecho_

    def setHijoDerecho(self, hijoDerecho):
        self._hijoDerecho_ = hijoDerecho
