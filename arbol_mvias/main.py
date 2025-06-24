from arbol import ArbolMVias

if __name__ == "__main__":
    arbol = ArbolMVias(3)
    for valor in [100, 80, 120, 70, 90, 110, 130]:
        arbol.insertar(valor)

    print("InOrden:")
    arbol.inOrden()

    print("PreOrden:")
    arbol.preOrden()

    print("PostOrden:")
    arbol.postOrden()

    print("Cantidad de nodos:", arbol.contarNodos())

    print("\nDFS:")
    arbol.dfs()

    print("BFS:")
    arbol.bfs()

    print("\nBuscar 90:", arbol.buscar(90))
    print("Buscar 999:", arbol.buscar(999))

    print("\nEliminando 70 (hoja):")
    arbol.eliminar(70)
    arbol.inOrden()

    print("\nEliminando 80 (con un hijo):")
    arbol.eliminar(80)
    arbol.inOrden()

    print("\nEliminando 100 (con dos hijos):")
    arbol.eliminar(100)
    arbol.inOrden()

