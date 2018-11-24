import numpy as np
import sys
import skfuzzy as fuzzy
from skfuzzy import control as ctrl

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
