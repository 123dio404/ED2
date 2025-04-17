from nodo import Nodo
from collections import deque

class ArbolBinario:
    def __init__(self):
        self._raiz_ = None

    def insertarNodo(self, x):
        self._raiz_ = self.__insertarNodoRecursivo(self._raiz_, x)

    def __insertarNodoRecursivo(self, nodoRaiz, x):
        if nodoRaiz is None:
            return Nodo(x)
        if x < nodoRaiz.getDato():
            nodoRaiz.setHijoIzquierdo(self.__insertarNodoRecursivo(nodoRaiz.getHijoIzquierdo(), x))
        else:
            nodoRaiz.setHijoDerecho(self.__insertarNodoRecursivo(nodoRaiz.getHijoDerecho(), x))
        return nodoRaiz

    def recorridoInOrden(self):
        self.__inOrden(self._raiz_)
        print()

    def __inOrden(self, nodo):
        if nodo:
            self.__inOrden(nodo.getHijoIzquierdo())
            print(nodo.getDato(), end=" ")
            self.__inOrden(nodo.getHijoDerecho())

    def recorridoPreOrden(self):
        self.__preOrden(self._raiz_)
        print()

    def __preOrden(self, nodo):
        if nodo:
            print(nodo.getDato(), end=" ")
            self.__preOrden(nodo.getHijoIzquierdo())
            self.__preOrden(nodo.getHijoDerecho())

    def recorridoPostOrden(self):
        self.__postOrden(self._raiz_)
        print()

    def __postOrden(self, nodo):
        if nodo:
            self.__postOrden(nodo.getHijoIzquierdo())
            self.__postOrden(nodo.getHijoDerecho())
            print(nodo.getDato(), end=" ")

    def contarNodos(self):
        return self.__contarNodos(self._raiz_)

    def __contarNodos(self, nodo):
        if nodo is None:
            return 0
        return 1 + self.__contarNodos(nodo.getHijoIzquierdo()) + self.__contarNodos(nodo.getHijoDerecho())

    def isVacio(self):
        return self._raiz_ is None

    def isHoja(self, nodo):
        return nodo.getHijoIzquierdo() is None and nodo.getHijoDerecho() is None

    def DFS(self):
        print("DFS (preorden):")
        self.__preOrden(self._raiz_)
        print()

    def BFS(self):
        print("BFS (nivel por nivel):")
        if self._raiz_ is None:
            return
        cola = deque()
        cola.append(self._raiz_)
        while cola:
            nodo = cola.popleft()
            print(nodo.getDato(), end=" ")
            if nodo.getHijoIzquierdo():
                cola.append(nodo.getHijoIzquierdo())
            if nodo.getHijoDerecho():
                cola.append(nodo.getHijoDerecho())
        print()

    # -------------------- FUNCIONES PARA ELIMINAR --------------------

    # Buscar un nodo con un valor dado
    def buscar(self, x):
        actual = self._raiz_
        while actual is not None:
            if x == actual.getDato():
                return actual
            elif x < actual.getDato():
                actual = actual.getHijoIzquierdo()
            else:
                actual = actual.getHijoDerecho()
        return None

    # Caso 1: Verifica si el nodo es hoja
    def EsHoja(self, nodo):
        return nodo.getHijoIzquierdo() is None and nodo.getHijoDerecho() is None

    # Caso 2: Verifica si el nodo tiene solo un hijo
    def EsIncompleto(self, nodo):
        return (nodo.getHijoIzquierdo() is None) != (nodo.getHijoDerecho() is None)

    # Caso 3: Verifica si el nodo tiene dos hijos
    def EsCompleto(self, nodo):
        return nodo.getHijoIzquierdo() is not None and nodo.getHijoDerecho() is not None

    # Buscar el padre de un nodo
    def buscarPadre(self, actual, nodo):
        if actual is None or actual == nodo:
            return None
        if actual.getHijoIzquierdo() == nodo or actual.getHijoDerecho() == nodo:
            return actual
        if nodo.getDato() < actual.getDato():
            return self.buscarPadre(actual.getHijoIzquierdo(), nodo)
        else:
            return self.buscarPadre(actual.getHijoDerecho(), nodo)

    # Eliminar nodo hoja (caso 1)
    def eliminar1(self, nodo):
        padre = self.buscarPadre(self._raiz_, nodo)
        if padre is not None:
            if padre.getHijoIzquierdo() == nodo:
                padre.setHijoIzquierdo(None)
            else:
                padre.setHijoDerecho(None)
        else:
            self._raiz_ = None

    # Eliminar nodo con un solo hijo (caso 2)
    def eliminar2(self, nodo):
        hijo = nodo.getHijoIzquierdo() if nodo.getHijoIzquierdo() else nodo.getHijoDerecho()
        padre = self.buscarPadre(self._raiz_, nodo)
        if padre is not None:
            if padre.getHijoIzquierdo() == nodo:
                padre.setHijoIzquierdo(hijo)
            else:
                padre.setHijoDerecho(hijo)
        else:
            self._raiz_ = hijo

    # Buscar el sucesor inmediato (el menor en el subárbol derecho)
    def EncontrarSucesor(self, nodo):
        actual = nodo.getHijoDerecho()
        while actual.getHijoIzquierdo():
            actual = actual.getHijoIzquierdo()
        return actual

    # Método general de eliminación
    def eliminar(self, x):
        nodo = self.buscar(x)
        if nodo is not None:
            if self.EsHoja(nodo):                # Caso 1: es hoja
                self.eliminar1(nodo)
            elif self.EsIncompleto(nodo):        # Caso 2: tiene un hijo
                self.eliminar2(nodo)
            elif self.EsCompleto(nodo):          # Caso 3: tiene dos hijos
                sucesor = self.EncontrarSucesor(nodo)
                nodo.setDato(sucesor.getDato())
                self.eliminar(sucesor.getDato())