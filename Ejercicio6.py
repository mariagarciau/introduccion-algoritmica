def descuento(microprocesadores=int(input("Cuantos microprocesadires has pedido ")),
    COMMAQ=bool(input("Eres cliente COMMAQ ")),BEL=bool(input("Eres cliente BEL "))):
    if microprocesadores>=10000 and microprocesadores<=20000:
        descuentoTotal=10
        if COMMAQ==True and BEL==False:
            descuentoTotal-=2
        elif BEL==True and COMMAQ==False:
            descuentoTotal+=1
        elif COMMAQ==True and BEL==True:
            descuentoTotal-=1
    elif microprocesadores>20000 and microprocesadores<=40000:
        if COMMAQ:
            descuentoTotal=13
        elif BEL:
            descuentoTotal=16
        elif COMMAQ and BEL:
            descuentoTotal=14
        elif not COMMAQ and not BEL:
            descuentoTotal=15
    elif microprocesadores>40000:
        if COMMAQ:
            descuentoTotal=18
        elif BEL:
            descuentoTotal=21
        elif COMMAQ and BEL:
            descuentoTotal=19
        elif not COMMAQ and not BEL:
            descuentoTotal=20
    return print(descuentoTotal)
descuento()