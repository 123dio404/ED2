from nodo import Nodo

class ArbolBinario:

    # Constructor de la clase ArbolBinario
    def __init__(self):
        self._raiz_ = None

    #insertar Nodo (Procedimiento)
    def insertarNodo(self, x):
        self._raiz_ = self.__insertarNodoRecursivo(self._raiz_, x)

    def __insertarNodoRecursivo(self, nodoRaiz,x):
        #Caso base
        if(nodoRaiz == None):
            return Nodo(x)
        else:
            if( x < nodoRaiz.getDato()): #en el caso que es Menor que el nodo raiz
                nodoRaiz.setHijoIzquierdo(self.__insertarNodoRecursivo(nodoRaiz.getHijoIzquierdo(), x))
            else: #en el caso que es Mayor que el nodo raiz
                nodoRaiz.setHijoDerecho(self.__insertarNodoRecursivo(nodoRaiz.getHijoDerecho(), x))

        #Retorna el nodo raiz
        return nodoRaiz
    
    def recorridoInOrden(self):
        self.__recorridoInOrdenRecursivo(self._raiz_)

    
    def __recorridoInOrdenRecursivo(self, nodoRaiz):
        if nodoRaiz is not None:
            self.__recorridoInOrdenRecursivo(nodoRaiz.getHijoIzquierdo())
            print(nodoRaiz.getDato(), end=" ")
            self.__recorridoInOrdenRecursivo(nodoRaiz.getHijoDerecho())

     
    def recorridoPreOrden(self):
        self.__recorridoPreOrdenRecursivo(self._raiz_)
    
    def __recorridoPreOrdenRecursivo(self, nodoRaiz):
        if nodoRaiz is not None:
            print(nodoRaiz.getDato(), end=" ")
            self.__recorridoPreOrdenRecursivo(nodoRaiz.getHijoIzquierdo())
            self.__recorridoPreOrdenRecursivo(nodoRaiz.getHijoDerecho())

     
    def recorridoPostOrden(self):
        self.__recorridoPostOrdenRecursivo(self._raiz_)
    
    def __recorridoPostOrdenRecursivo(self, nodoRaiz):
        if nodoRaiz is not None:
            self.__recorridoPostOrdenRecursivo(nodoRaiz.getHijoIzquierdo())
            self.__recorridoPostOrdenRecursivo(nodoRaiz.getHijoDerecho())
            print(nodoRaiz.getDato(), end=" ")
    

    def isVacio(self):
        return self._raiz_ == None

    def isHoja(self, nodoRaiz):
        return nodoRaiz.getHijoIzquierdo() == None and nodoRaiz.getHijoDerecho() == None

    def contarNodos(self):
        return self.__contarNodosRecursivo(self._raiz_)
    
    def __contarNodosRecursivo(self, nodoRaizAux):
        if(nodoRaizAux == None): #Caso Base ARbol Vacio
            return 0
        else:
            if(self.isHoja(nodoRaizAux)):#Caso base ARbol tiene 1 solo Nodo
                return 1
            else: # Caso General
                i = self.__contarNodosRecursivo(nodoRaizAux.getHijoIzquierdo()) #2
                d = self.__contarNodosRecursivo(nodoRaizAux.getHijoDerecho())  #1
                return d + i + 1


if __name__ == "__main__":
    arbol = ArbolBinario()
    arbol.insertarNodo(100)
    arbol.insertarNodo(80)
    arbol.insertarNodo(120)
    arbol.insertarNodo(70)
    arbol.recorridoInOrden()  # Salida: 70 80 100 120
    print()
    arbol.recorridoPreOrden() 
    print()
    arbol.recorridoPostOrden() 
   
    print()
    print("Cantidad de nodos:", arbol.contarNodos())