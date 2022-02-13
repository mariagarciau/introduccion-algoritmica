def primaAnual(prima):
    responsabilidad=int(input("Cuanta responsabilidad sobre el accidente tiene "))
    numeroAccidentes=int(input("Cuantos accidentes ha tenido "))
    distancia=int(input("Cuantos km ha recorrido "))
    añosAntigüedad=int(input("Cuantos años lleva "))
    if responsabilidad<=20:
        prima=prima
        if 0.01*distancia<=400:
            prima=prima+0.01*distancia
        if añosAntigüedad>=4:
            prima=prima+200+(añosAntigüedad-4)*20
    elif responsabilidad>20:
        if numeroAccidentes==1:
            prima=prima/2
            if 0.01*distancia<=400:
                prima=prima+0.01*distancia
            if añosAntigüedad>=4:
                prima=prima+200+(añosAntigüedad-4)*20
        elif numeroAccidentes==2:
            prima=prima/3
            if 0.01*distancia<=400:
                prima=prima+0.01*distancia
            if añosAntigüedad>=4:
                prima=prima+200+(añosAntigüedad-4)*20
        elif numeroAccidentes==3:
            prima=prima/4
            if 0.01*distancia<=400:
                prima=prima+0.01*distancia
            if añosAntigüedad>=4:
                prima=prima+200+(añosAntigüedad-4)*20
        elif numeroAccidentes>3:
            prima=0
            if 0.01*distancia<=400:
                prima=prima+0.01*distancia
            if añosAntigüedad>=4:
                prima=prima+200+(añosAntigüedad-4)*20
    return print(prima)
primaAnual(10)
