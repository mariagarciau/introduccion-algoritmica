from enum import Enum
class DIA(Enum):
    LUNES=0
    MARTES=1
    MIERCOLES=2
    JUEVES=3
    VIERNES=4
    SABADO=5
    DOMINGO=6
def sucesor():
    if DIA.LUNES:
        dia=DIA.MARTES
    elif DIA.MARTES:
        dia=DIA.MIERCOLES
    elif DIA.MIERCOLES:
        dia=DIA.JUEVES
    elif DIA.JUEVES:
        dia=DIA.VIERNES
    elif DIA.VIERNES:
        dia=DIA.SABADO
    elif DIA.SABADO:
        dia=DIA.DOMINGO
    elif DIA.DOMINGO:
        dia=DIA.LUNES
    return print(dia)
sucesor()

