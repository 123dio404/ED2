class Nodo:
    """
    Representa un nodo de un Árbol Binario de Búsqueda.
    Contiene un dato y referencias a sus hijos izquierdo y derecho.
    """
    def __init__(self, dato):
        self.dato = dato  # Valor almacenado en el nodo
        self.izquierdo = None  # Referencia al hijo izquierdo
        self.derecho = None  # Referencia al hijo derecho
    
    def get_dato(self):
        """ Devuelve el dato del nodo. """
        return self.dato
    
    def set_dato(self, dato):
        """ Asigna un nuevo valor al nodo. """
        self.dato = dato
    
    def get_izquierdo(self):
        """ Devuelve la referencia al hijo izquierdo. """
        return self.izquierdo
    
    def set_izquierdo(self, nodo):
        """ Asigna un nodo como hijo izquierdo. """
        self.izquierdo = nodo
    
    def get_derecho(self):
        """ Devuelve la referencia al hijo derecho. """
        return self.derecho
    
    def set_derecho(self, nodo):
        """ Asigna un nodo como hijo derecho. """
        self.derecho = nodo
