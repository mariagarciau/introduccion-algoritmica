def descuento(microprocesadores=int(input("Cuantos microprocesadires has pedido "))):
    COMMAQ=str(input("Eres cliente COMMAQ "))
    BEL=str(input("Eres cliente BEL "))
    if microprocesadores>=10000 and microprocesadores<=20000:
        descuentoTotal=10
        if COMMAQ=="si" and BEL=="no":
            descuentoTotal-=2
        elif COMMAQ=="no" and BEL=="si" :
            descuentoTotal+=1
        elif COMMAQ=="si" and BEL=="si":
            descuentoTotal-=1
    elif microprocesadores>20000 and microprocesadores<=40000:
        descuentoTotal=15
        if COMMAQ=="si" and BEL=="no":
            descuentoTotal-=2
        elif COMMAQ=="no" and BEL=="si" :
            descuentoTotal+=1
        elif COMMAQ=="si" and BEL=="si":
            descuentoTotal-=1
    elif microprocesadores>40000:
        descuentoTotal=20
        if COMMAQ=="si" and BEL=="no":
            descuentoTotal-=2
        elif COMMAQ=="no" and BEL=="si" :
            descuentoTotal+=1
        elif COMMAQ=="si" and BEL=="si":
            descuentoTotal-=1
    return print(descuentoTotal)
descuento()