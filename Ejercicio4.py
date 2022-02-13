def media(n1=int(input("introduce la nota ")),n2=int(input("introduce la nota ")),
    n3=int(input("introduce la nota ")),n4=int(input("introduce la nota "))):
    notaMedia=(n1+n2+n3+n4)/4
    if notaMedia>15:
        return print("Alumno con talento")
    elif notaMedia>=12 and notaMedia<=15:
        return print("Con capacidad")
    elif notaMedia<12:
        return print("Debe reorientarse")
media()

