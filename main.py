if __name__ == '__main__':
    import coloresRepetidos
    import numpy as np
    import sys
    import skfuzzy as fuzzy
    from skfuzzy import control as ctrl

    colores_repetidos, hsv, porcentage = coloresRepetidos.colores(
        str(sys.argv[1]))
    brillo = ctrl.Antecedent(np.arange(0, 101, 1), 'brillo')
    saturacion = ctrl.Antecedent(np.arange(0, 101, 1), 'saturacion')
    repeticion = ctrl.Antecedent(np.arange(0, 101, 0.1), 'repeticion')
    paleta = ctrl.Consequent(np.arange(0, 101, 1), 'paleta')

    repeticion['poco'] = fuzzy.trimf(repeticion.universe, [0, 0, 2.5])
    repeticion['medio'] = fuzzy.trimf(repeticion.universe, [2.0, 5.5, 8.5])
    repeticion['mucho'] = fuzzy.trimf(repeticion.universe, [6.5, 100, 100])

    brillo['oscuro'] = fuzzy.trimf(brillo.universe, [0, 0, 30])
    brillo['medio'] = fuzzy.trimf(brillo.universe, [25, 50, 70])
    brillo['Brillante'] = fuzzy.trimf(brillo.universe, [60, 100, 100])

    saturacion['debil'] = fuzzy.trimf(saturacion.universe, [0, 0, 20])
    saturacion['moderado'] = fuzzy.trimf(saturacion.universe, [15, 50, 75])
    saturacion['intenso'] = fuzzy.trimf(saturacion.universe, [70, 100, 100])

    paleta['no'] = fuzzy.trimf(paleta.universe, [0, 0, 51])
    paleta['si'] = fuzzy.trimf(paleta.universe, [50, 100, 100])

    rule1 = ctrl.Rule(
        repeticion['poco'] & brillo['oscuro'] & saturacion['debil'], paleta['no'])
    rule2 = ctrl.Rule(
        repeticion['medio'] & brillo['medio'] & saturacion['debil'], paleta['no'])
    rule3 = ctrl.Rule(
        repeticion['mucho'] & brillo['Brillante'] & saturacion['debil'], paleta['si'])
    rule4 = ctrl.Rule(
        repeticion['poco'] & brillo['oscuro'] & saturacion['moderado'], paleta['no'])
    rule5 = ctrl.Rule(
        repeticion['medio'] & brillo['medio'] & saturacion['moderado'], paleta['si'])
    rule6 = ctrl.Rule(
        repeticion['mucho'] & brillo['Brillante'] & saturacion['moderado'], paleta['si'])
    rule7 = ctrl.Rule(
        repeticion['poco'] & brillo['oscuro'] & saturacion['intenso'], paleta['no'])
    rule8 = ctrl.Rule(
        repeticion['medio'] & brillo['medio'] & saturacion['intenso'], paleta['si'])
    rule9 = ctrl.Rule(
        repeticion['mucho'] & brillo['Brillante'] & saturacion['intenso'], paleta['si'])
    rule10 = ctrl.Rule(
        repeticion['poco'] & brillo['oscuro'] & saturacion['debil'], paleta['no'])
    rule11 = ctrl.Rule(
        repeticion['medio'] & brillo['oscuro'] & saturacion['moderado'], paleta['no'])
    rule12 = ctrl.Rule(
        repeticion['mucho'] & brillo['oscuro'] & saturacion['intenso'], paleta['si'])
    rule13 = ctrl.Rule(
        repeticion['poco'] & brillo['medio'] & saturacion['debil'], paleta['no'])
    rule14 = ctrl.Rule(
        repeticion['medio'] & brillo['medio'] & saturacion['moderado'], paleta['si'])
    rule15 = ctrl.Rule(
        repeticion['mucho'] & brillo['medio'] & saturacion['intenso'], paleta['si'])
    rule16 = ctrl.Rule(
        repeticion['poco'] & brillo['Brillante'] & saturacion['debil'], paleta['no'])
    rule17 = ctrl.Rule(
        repeticion['medio'] & brillo['Brillante'] & saturacion['moderado'], paleta['no'])
    rule18 = ctrl.Rule(
        repeticion['mucho'] & brillo['Brillante'] & saturacion['intenso'], paleta['si'])
    rule19 = ctrl.Rule(
        repeticion['poco'] & brillo['oscuro'] & saturacion['debil'], paleta['no'])
    rule20 = ctrl.Rule(
        repeticion['poco'] & brillo['medio'] & saturacion['moderado'], paleta['no'])
    rule21 = ctrl.Rule(
        repeticion['poco'] & brillo['Brillante'] & saturacion['intenso'], paleta['si'])
    rule22 = ctrl.Rule(
        repeticion['medio'] & brillo['oscuro'] & saturacion['debil'], paleta['no'])
    rule23 = ctrl.Rule(
        repeticion['medio'] & brillo['medio'] & saturacion['moderado'], paleta['no'])
    rule24 = ctrl.Rule(
        repeticion['medio'] & brillo['Brillante'] & saturacion['intenso'], paleta['si'])
    rule25 = ctrl.Rule(
        repeticion['mucho'] & brillo['oscuro'] & saturacion['debil'], paleta['no'])
    rule26 = ctrl.Rule(
        repeticion['mucho'] & brillo['medio'] & saturacion['moderado'], paleta['si'])
    rule27 = ctrl.Rule(
        repeticion['mucho'] & brillo['Brillante'] & saturacion['intenso'], paleta['si'])
    rule28 = ctrl.Rule(
        repeticion['poco'] & brillo['medio'] & saturacion['intenso'], paleta['no'])
    rule29 = ctrl.Rule(
        repeticion['poco'] & brillo['Brillante'] & saturacion['moderado'], paleta['no'])
    rule30 = ctrl.Rule(
        repeticion['poco'] & brillo['Brillante'] & saturacion['intenso'], paleta['no'])
    rule31 = ctrl.Rule(
        repeticion['medio'] & brillo['Brillante'] & saturacion['debil'], paleta['no'])
    # print(colores_repetidos, hsv,  len(colores_repetidos))
    reglas = [rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10,
              rule11, rule12, rule13, rule14, rule15, rule16, rule17, rule18, rule19,
              rule20, rule21, rule22, rule23, rule24, rule25, rule26, rule27, rule28, rule29, rule30, rule31]
    paleta_ctrl = ctrl.ControlSystem(reglas)
    paletaa = ctrl.ControlSystemSimulation(paleta_ctrl)

    paleta_de_colores = []

    for i in range(0, len(hsv)):
        # print("saturacion", (hsv[i][0][0][1] * 100) / 255, "brillo", (hsv[i][0][0]
                                                                      # [2] * 100) / 255, "repeticion", float("{0:.1f}". format(porcentage[i])))
        paletaa.input['saturacion'] = (hsv[i][0][0][1] * 100) / 255
        paletaa.input['brillo'] = (hsv[i][0][0][2] * 100) / 255
        paletaa.input['repeticion'] = float("{0:.1f}". format(porcentage[i]))
        paletaa.compute()
        if paletaa.output['paleta'] > 50:
            paleta_de_colores.append(colores_repetidos[i])

    for color in paleta_de_colores:
        print(color)
