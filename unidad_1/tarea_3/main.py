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

    print("InOrden original:")
    arbol.recorridoInOrden()

    print("\nPreOrden original:")
    arbol.recorridoPreOrden()

    print("\nPostOrden original:")
    arbol.recorridoPostOrden()

    print("\nCantidad de nodos:", arbol.contarNodos())

    print("\nDFS:")
    arbol.DFS()
    print("BFS:")
    arbol.BFS()

    # 🔻 Caso 1: eliminar nodo hoja (70)
    print("\nEliminando nodo hoja (70):")
    arbol.eliminar(70)
    arbol.recorridoInOrden()

    # 🔻 Caso 2: eliminar nodo con un hijo (80 ahora solo tiene 90)
    print("\nEliminando nodo con un hijo (80):")
    arbol.eliminar(80)
    arbol.recorridoInOrden()

    # 🔻 Caso 3: eliminar nodo con dos hijos (100 tiene 90 e 120)
    print("\nEliminando nodo con dos hijos (100):")
    arbol.eliminar(100)
    arbol.recorridoInOrden()
