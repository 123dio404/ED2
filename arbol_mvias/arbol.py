from nodo import NodoMVias

def crearNodo(m):
    return NodoMVias(m)

class ArbolMVias:
    def __init__(self, orden):
        self.raiz = None
        self.orden = orden

    def insertar(self, dato):
        if self.raiz is None:
            self.raiz = crearNodo(self.orden)
            self.raiz.datos.append(dato)
            return
        self._insertar(self.raiz, dato)
        
    def _insertar(self, nodo, dato):
     if nodo.estaLleno():
        # Redirigir al hijo adecuado (crearlo si no existe)
        for i in range(len(nodo.datos)):
            if dato < nodo.datos[i]:
                if i < len(nodo.hijos) and nodo.hijos[i]:
                    self._insertar(nodo.hijos[i], dato)
                else:
                    nuevo = crearNodo(self.orden)
                    nuevo.datos.append(dato)
                    if i < len(nodo.hijos):
                        nodo.hijos[i] = nuevo
                    else:
                        while len(nodo.hijos) <= i:
                            nodo.hijos.append(None)
                        nodo.hijos[i] = nuevo
                return
        # Insertar en el último hijo
        idx = len(nodo.datos)
        if idx < len(nodo.hijos) and nodo.hijos[idx]:
            self._insertar(nodo.hijos[idx], dato)
        else:
            nuevo = crearNodo(self.orden)
            nuevo.datos.append(dato)
            while len(nodo.hijos) <= idx:
                nodo.hijos.append(None)
            nodo.hijos[idx] = nuevo
     else:
        nodo.datos.append(dato)
        nodo.datos.sort()
        while len(nodo.hijos) < len(nodo.datos) + 1:
            nodo.hijos.append(None)


    def inOrden(self):
        self._inOrden(self.raiz)
        print()

    def _inOrden(self, nodo):
        if nodo:
            for i in range(len(nodo.datos)):
                if i < len(nodo.hijos) and nodo.hijos[i]:
                    self._inOrden(nodo.hijos[i])
                print(nodo.datos[i], end=" ")
            if len(nodo.hijos) > len(nodo.datos) and nodo.hijos[-1]:
                self._inOrden(nodo.hijos[-1])

    def preOrden(self):
        self._preOrden(self.raiz)
        print()

    def _preOrden(self, nodo):
        if nodo:
            for dato in nodo.datos:
                print(dato, end=" ")
            for hijo in nodo.hijos:
                if hijo:
                    self._preOrden(hijo)

    def postOrden(self):
        self._postOrden(self.raiz)
        print()

    def _postOrden(self, nodo):
        if nodo:
            for hijo in nodo.hijos:
                if hijo:
                    self._postOrden(hijo)
            for dato in nodo.datos:
                print(dato, end=" ")

    def contarNodos(self):
        return self._contarNodos(self.raiz)

    def _contarNodos(self, nodo):
        if nodo is None:
            return 0
        total = 1
        for hijo in nodo.hijos:
            if hijo:
                total += self._contarNodos(hijo)
        return total

    def bfs(self):
        if self.raiz is None:
            return
        cola = [self.raiz]
        while cola:
            actual = cola.pop(0)
            for dato in actual.datos:
                print(dato, end=" ")
            for hijo in actual.hijos:
                if hijo:
                    cola.append(hijo)
        print()

    def dfs(self):
        self._dfs(self.raiz)
        print()

    def _dfs(self, nodo):
        if nodo:
            for dato in nodo.datos:
                print(dato, end=" ")
            for hijo in nodo.hijos:
                if hijo:
                    self._dfs(hijo)

    def buscar(self, dato):
        return self._buscar(self.raiz, dato)

    def _buscar(self, nodo, dato):
        if nodo is None:
            return False
        if dato in nodo.datos:
            return True
        for i in range(len(nodo.datos)):
            if dato < nodo.datos[i]:
                if i < len(nodo.hijos) and nodo.hijos[i]:
                    return self._buscar(nodo.hijos[i], dato)
                return False
        if len(nodo.hijos) > len(nodo.datos) and nodo.hijos[-1]:
            return self._buscar(nodo.hijos[-1], dato)
        return False

    def eliminar(self, dato):
        self.raiz = self._eliminar(self.raiz, dato)

    def _eliminar(self, nodo, dato):
        if nodo is None:
            return None

        if dato in nodo.datos:
            idx = nodo.datos.index(dato)
            if nodo.esHoja():
                nodo.datos.remove(dato)
            else:
                sucesor = self._minimoSeguro(nodo.hijos[idx + 1])
                if sucesor is not None:
                    nodo.datos[idx] = sucesor
                    nodo.hijos[idx + 1] = self._eliminar(nodo.hijos[idx + 1], sucesor)
        else:
            for i in range(len(nodo.datos)):
                if dato < nodo.datos[i]:
                    nodo.hijos[i] = self._eliminar(nodo.hijos[i], dato)
                    return nodo
            nodo.hijos[len(nodo.datos)] = self._eliminar(nodo.hijos[len(nodo.datos)], dato)

        if not nodo.datos and nodo.esHoja():
            return None
        return nodo

    def _minimoSeguro(self, nodo):
        actual = nodo
        while actual is not None and not actual.esHoja():
            actual = actual.hijos[0]
        if actual and actual.datos:
            return actual.datos[0]
        return None

