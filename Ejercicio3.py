def descuento(precio=int(input("introduzca el precio "))):
    if precio>=100 and precio<=500:
        precio=precio-precio*0.05
    elif precio>=800:
        precio=precio-precio*0.08
    else:
        precio=precio
    return print(precio)
descuento()

