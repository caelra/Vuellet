import numpy as np
import sys
import skfuzzy as fuzzy
from skfuzzy import control as ctrl
from conjuntos import *

RULE1 = ctrl.Rule(
    repeticion['poco'] & brillo['oscuro'] & saturacion['debil'], paleta['no'])
RULE2 = ctrl.Rule(
    repeticion['medio'] & brillo['medio'] & saturacion['debil'], paleta['no'])
RULE3 = ctrl.Rule(
    repeticion['mucho'] & brillo['Brillante'] & saturacion['debil'], paleta['si'])
RULE4 = ctrl.Rule(
    repeticion['poco'] & brillo['oscuro'] & saturacion['moderado'], paleta['no'])
RULE5 = ctrl.Rule(
    repeticion['medio'] & brillo['medio'] & saturacion['moderado'], paleta['si'])
RULE6 = ctrl.Rule(
    repeticion['mucho'] & brillo['Brillante'] & saturacion['moderado'], paleta['si'])
RULE7 = ctrl.Rule(
    repeticion['poco'] & brillo['oscuro'] & saturacion['intenso'], paleta['no'])
RULE8 = ctrl.Rule(
    repeticion['medio'] & brillo['medio'] & saturacion['intenso'], paleta['si'])
RULE9 = ctrl.Rule(
    repeticion['mucho'] & brillo['Brillante'] & saturacion['intenso'], paleta['si'])
RULE10 = ctrl.Rule(
    repeticion['poco'] & brillo['oscuro'] & saturacion['debil'], paleta['no'])
RULE11 = ctrl.Rule(
    repeticion['medio'] & brillo['oscuro'] & saturacion['moderado'], paleta['no'])
RULE12 = ctrl.Rule(
    repeticion['mucho'] & brillo['oscuro'] & saturacion['intenso'], paleta['si'])
RULE13 = ctrl.Rule(
    repeticion['poco'] & brillo['medio'] & saturacion['debil'], paleta['no'])
RULE14 = ctrl.Rule(
    repeticion['medio'] & brillo['medio'] & saturacion['moderado'], paleta['si'])
RULE15 = ctrl.Rule(
    repeticion['mucho'] & brillo['medio'] & saturacion['intenso'], paleta['si'])
RULE16 = ctrl.Rule(
    repeticion['poco'] & brillo['Brillante'] & saturacion['debil'], paleta['no'])
RULE17 = ctrl.Rule(
    repeticion['medio'] & brillo['Brillante'] & saturacion['moderado'], paleta['si'])
RULE18 = ctrl.Rule(
    repeticion['mucho'] & brillo['Brillante'] & saturacion['intenso'], paleta['si'])
RULE19 = ctrl.Rule(
    repeticion['poco'] & brillo['oscuro'] & saturacion['debil'], paleta['no'])
RULE20 = ctrl.Rule(
    repeticion['poco'] & brillo['medio'] & saturacion['moderado'], paleta['no'])
RULE21 = ctrl.Rule(
    repeticion['poco'] & brillo['Brillante'] & saturacion['intenso'], paleta['si'])
RULE22 = ctrl.Rule(
    repeticion['medio'] & brillo['oscuro'] & saturacion['debil'], paleta['no'])
RULE23 = ctrl.Rule(
    repeticion['medio'] & brillo['medio'] & saturacion['moderado'], paleta['si'])
RULE24 = ctrl.Rule(
    repeticion['medio'] & brillo['Brillante'] & saturacion['intenso'], paleta['si'])
RULE25 = ctrl.Rule(
    repeticion['mucho'] & brillo['oscuro'] & saturacion['debil'], paleta['no'])
RULE26 = ctrl.Rule(
    repeticion['mucho'] & brillo['medio'] & saturacion['moderado'], paleta['si'])
RULE27 = ctrl.Rule(
    repeticion['mucho'] & brillo['Brillante'] & saturacion['intenso'], paleta['si'])
RULE28 = ctrl.Rule(
    repeticion['poco'] & brillo['medio'] & saturacion['intenso'], paleta['no'])
RULE29 = ctrl.Rule(
    repeticion['poco'] & brillo['Brillante'] & saturacion['moderado'], paleta['no'])
RULE30 = ctrl.Rule(
    repeticion['poco'] & brillo['Brillante'] & saturacion['intenso'], paleta['no'])
RULE31 = ctrl.Rule(
    repeticion['medio'] & brillo['Brillante'] & saturacion['debil'], paleta['no'])
RULE32 = ctrl.Rule(
    repeticion['mucho'] & brillo['oscuro'] & saturacion['moderado'], paleta['si'])
RULE33 = ctrl.Rule(
    repeticion['mucho'] & brillo['medio'] & saturacion['debil'], paleta['si'])
RULE34 = ctrl.Rule(
    repeticion['medio'] & brillo['oscuro'] & saturacion['intenso'], paleta['si'])

reglas = [RULE1, RULE2, RULE3, RULE4, RULE5, RULE6, RULE7, RULE8, RULE9, RULE10,
          RULE11, RULE12, RULE13, RULE14, RULE15, RULE16, RULE17, RULE18, RULE19,
          RULE20, RULE21, RULE22, RULE23, RULE24, RULE25, RULE26, RULE27, RULE28,
          RULE29, RULE30, RULE31, RULE32, RULE33, RULE34
          ]
