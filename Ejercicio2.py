def numeros(n1=int(input("introduce un numero ")),n2=int(input("introduce un numero "))):
    suma=n1+n2
    multiplicacion=n1*n2
    orden=[n1,n2,suma,multiplicacion]
    orden.sort()
    return print(orden)
numeros()