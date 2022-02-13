def descuento(niños=int(input("Cuantos niños son"))):
    precio=int(input("precio total"))
    if niños==2:
        precio= precio-precio*0.1
    elif niños==3:
        precio= precio-precio*0.15
    elif niños==4:
        precio= precio-precio*0.18
    elif niños>=5:
        precio=precio-precio*0.18-(niños-4)*0.01
    return print(precio)
descuento()
