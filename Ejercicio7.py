def viaje(alumnos=int(input("Cuantos alumnos van ")), dias=int(input("cuantos dias son "))):
    coste=0
    if alumnos<=25:
        coste=67.30*alumnos+3.5*alumnos*dias+4.75*alumnos*dias
        print(coste)
    elif alumnos>25 and alumnos<=30:
        coste=61*alumnos+3.5*alumnos*dias+4.75*alumnos*dias
    elif alumnos>=31 and alumnos<=35:
        coste=61*alumnos+3.5*alumnos*dias+4*alumnos*dias
    elif alumnos>35:
        coste=61*alumnos+3.5*alumnos*dias+3.5*alumnos*dias
    return print(coste)