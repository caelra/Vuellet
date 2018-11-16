def colores(imagen):
    """Devuelve cuales son los colores mas repetidos en una imagen, con un humbral de repeticion"""
    import cv2 as cv
    img = cv.imread(imagen, 1)
    colores = []
    colores.append(list(img[0][0]))
    for i in range(0, img.shape[0], 20):
        for j in range(0, img.shape[1], 20):
            todos_los_componentes = True
            for color in colores:
                if todos_los_componentes:
                    todos = 0
                    for rgb in range(len(img[i][j])):
                        if img[i][j][rgb] > color[rgb] - 30 and img[i][j][rgb] < color[rgb] + 30:
                            todos += 1
                    if todos > 2:
                        todos_los_componentes = False
            if todos_los_componentes:
                colores.append(list(img[i][j]))
    return colores


# colores_repetidos = coloresRepetidos('prueba.jpg')
# print(colores_repetidos, len(colores_repetidos))
