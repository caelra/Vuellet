def sistemaDifuso(imagen):
    import coloresRepetidos
    import numpy as np
    import sys
    import skfuzzy as fuzzy
    from skfuzzy import control as ctrl
    from reglas import reglas

    colores_repetidos, hsv, porcentage = coloresRepetidos.colores(imagen)
    paleta_ctrl = ctrl.ControlSystem(reglas)

    paletaa = ctrl.ControlSystemSimulation(paleta_ctrl)

    paleta_de_colores = []

    for i in range(0, len(hsv)):
        # se transforman los colores a valor de 100
        paletaa.input['saturacion'] = (hsv[i][0][0][1] * 100) / 255
        paletaa.input['brillo'] = (hsv[i][0][0][2] * 100) / 255
        # se redondean los decimales del porcentaje
        paletaa.input['repeticion'] = float("{0:.1f}". format(porcentage[i]))
        paletaa.compute()
        if paletaa.output['paleta'] > 50:
            paleta_de_colores.append(colores_repetidos[i])

    return paleta_de_colores
