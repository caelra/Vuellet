import cv2 as cv


def coloresRepetidos(imagen):
    """Devuelve cuales son los colores mas repetidos en una imagen, con un humbral de repeticion"""
    img = cv.imread(imagen, 1)
    colores = []
    colores.append(list(img[0][0]))
    for i in range(0, img.shape[0], 40):
        for j in range(0, img.shape[1], 40):
            for color in colores:
                red, green, blue = False, False, False
                for rgb in range(len(img[i][j])):
                    if img[i][j][rgb] > color[rgb] - 30 and img[i][j][rgb] < color[rgb] + 30:
                        if rgb == 0:
                            red = True
                        elif rgb == 1:
                            green = True
                        elif rgb == 2:
                            blue = True
            if red == False and green == False and blue == False:
                colores.append(list(img[i][j]))
    return colores


img = cv.imread('prueba.jpg', 1)
colores_repetidos = coloresRepetidos('prueba.jpg')
print(img.size)
print(colores_repetidos, len(colores_repetidos))
