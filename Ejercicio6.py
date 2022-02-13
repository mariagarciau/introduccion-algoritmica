def descuento(microprocesadores=int(input("Cuantos microprocesadires has pedido ")),
    COMMAQ=bool(input("Eres cliente COMMAQ ")),BEL=bool(input("Eres cliente BEL "))):
    if microprocesadores>=10000 and microprocesadores<=20000 and COMMAQ==False and BEL==False:
        descuentoTotal=10
        return print(descuentoTotal)
    elif microprocesadores>=10000 and microprocesadores<=20000 and COMMAQ==True and BEL==False:
        descuentoTotal=8
        return print(descuentoTotal)
    elif microprocesadores>=10000 and microprocesadores<=20000 and not COMMAQ and BEL:
        descuentoTotal=11
        return print(descuentoTotal)
    elif microprocesadores>=10000 and microprocesadores<=20000 and COMMAQ==True and BEL==True:
        descuentoTotal=9
        return print(descuentoTotal)
    elif microprocesadores>20000 and microprocesadores<=40000 and COMMAQ==False and BEL==False:
        descuentoTotal=15
        return print(descuentoTotal)
    elif microprocesadores>20000 and microprocesadores<=40000 and COMMAQ==True and BEL==False:
        descuentoTotal=13
        return print(descuentoTotal)
    elif microprocesadores>20000 and microprocesadores<=40000 and COMMAQ==False and BEL==True:
        descuentoTotal=16
        return print(descuentoTotal)
    elif microprocesadores>20000 and microprocesadores<=40000 and COMMAQ==True and BEL==True:
        descuentoTotal=14
        return print(descuentoTotal)
    elif microprocesadores>40000 and COMMAQ==False and BEL==False:
        descuentoTotal=20
        return print(descuentoTotal)
    elif microprocesadores>40000 and COMMAQ==True and BEL==False:
        descuentoTotal=18
        return print(descuentoTotal)
    elif microprocesadores>40000 and COMMAQ==False and BEL==True:
        descuentoTotal=21
        return print(descuentoTotal)
    elif microprocesadores>40000 and COMMAQ==True and BEL==True:
        descuentoTotal=19
        return print(descuentoTotal)
descuento()