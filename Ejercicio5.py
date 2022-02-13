def descuento(niños=int(input("Cuantos niños son "))):
    if niños==2:
        descuentoTotal=10
    elif niños==3:
        descuentoTotal=15
    elif niños==4:
        descuentoTotal=18
    elif niños>=5:
        descuentoTotal=18+(niños-4)*1
    return print(descuentoTotal)
descuento()
