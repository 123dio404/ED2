class NodoMVias:
    def __init__(self, orden):
        self.datos = []
        self.hijos = []
        self.orden = orden

    def estaLleno(self):
        return len(self.datos) >= self.orden - 1

    def esHoja(self):
        return len(self.hijos) == 0
