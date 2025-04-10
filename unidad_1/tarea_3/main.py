from arbol import ArbolBinario

if __name__ == "__main__":
    arbol = ArbolBinario()
    arbol.insertarNodo(100)
    arbol.insertarNodo(80)
    arbol.insertarNodo(120)
    arbol.insertarNodo(70)
    arbol.insertarNodo(90)
    arbol.insertarNodo(110)
    arbol.insertarNodo(130)

    print("InOrden:")
    arbol.recorridoInOrden()

    print("PreOrden:")
    arbol.recorridoPreOrden()

    print("PostOrden:")
    arbol.recorridoPostOrden()

    print("Cantidad de nodos:", arbol.contarNodos())

    arbol.DFS()
    arbol.BFS()
