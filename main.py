if __name__ == '__main__':
    import coloresRepetidos
    import sys
    print("hello word")
    # img = cv.imread('prueba.png', 1)
    colores_repetidos = coloresRepetidos.colores(str(sys.argv[1]))
    print(colores_repetidos, len(colores_repetidos))
