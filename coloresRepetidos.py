def colores(imagen):
    """Devuelve cuales son los colores mas repetidos en una imagen, con un humbral de repeticion"""
    import cv2 as cv
    import numpy as np
    img = cv.imread(imagen, 1)
    colores = []
    hsv = []
    repetidos = {}
    colores.append(list(img[0][0]))
    hsv.append(
        list(cv.cvtColor(np.uint8([[np.array(img[0][0])]]), cv.COLOR_BGR2HSV)))
    repetidos['color1'] = 1
    color_value = 1
    color_key = 'color'
    color_number = 0
    porcentage = []
    for i in range(0, img.shape[0], 10):
        for j in range(0, img.shape[1], 10):
            color_number += 1
            todos_los_componentes = True
            for color in colores:
                if todos_los_componentes:
                    todos = 0
                    for rgb in range(len(img[i][j])):
                        if img[i][j][rgb] > color[rgb] - 30 and img[i][j][rgb] < color[rgb] + 30:
                            todos += 1
                    if todos > 2:
                        todos_los_componentes = False
                        repetidos[color_key + str(color_value)] += 1
            if todos_los_componentes:
                color_value += 1
                repetidos[color_key + str(color_value)] = 1
                colores.append(list(img[i][j]))
                hsv_helper = (cv.cvtColor(
                    np.uint8([[(img[i][j])]]), cv.COLOR_BGR2HSV))
                hsv.append(hsv_helper)
    for key, value in repetidos.items():

        porcentage.append((value * 100) / color_number)
    return colores, hsv, porcentage
