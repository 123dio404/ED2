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
