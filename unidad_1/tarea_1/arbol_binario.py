from nodo import Nodo  # Importamos la clase Nodo

class ArbolBinario:
    """
    Implementa un Árbol Binario de Búsqueda (ABB).
    Permite insertar elementos y recorrerlos en orden.
    """
    def __init__(self):
        self.raiz = None  # Raíz del árbol
    
    def get_raiz(self):
        """ Devuelve la raíz del árbol. """
        return self.raiz
    
    def set_raiz(self, nodo):
        """ Asigna un nodo como la raíz del árbol. """
        self.raiz = nodo
    
    def insertar(self, dato):
        """ Inserta un nuevo dato en el árbol. """
        self.raiz = self._insertar_rec(self.raiz, dato)
    
    def _insertar_rec(self, nodo, dato):
        """ Inserta un dato de manera recursiva en el árbol. """
        if nodo is None:
            return Nodo(dato)
        if dato < nodo.get_dato():
            nodo.set_izquierdo(self._insertar_rec(nodo.get_izquierdo(), dato))
        else:
            nodo.set_derecho(self._insertar_rec(nodo.get_derecho(), dato))
        return nodo
    
    def in_orden(self):
        """ Recorre el árbol en orden y muestra los valores. """
        self._in_orden_rec(self.raiz)
        print()
    
    def _in_orden_rec(self, nodo):
        """ Recorre el árbol en orden de manera recursiva e imprime los valores en orden creciente. """
        if nodo is not None:
            self._in_orden_rec(nodo.get_izquierdo())
            print(str(nodo.get_dato()) + ' ', end='')
            self._in_orden_rec(nodo.get_derecho())

if __name__ == "__main__":
    """
    Prueba del Árbol Binario de Búsqueda.
    Se insertan varios valores y se muestra el recorrido en orden.
    """
    arbol = ArbolBinario()
    arbol.insertar(50)
    arbol.insertar(30)
    arbol.insertar(70)
    arbol.insertar(20)
    arbol.insertar(40)
    arbol.insertar(60)
    arbol.insertar(80)
    
    print("Recorrido en orden:")
    arbol.in_orden()
