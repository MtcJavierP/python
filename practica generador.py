#primero funcion tradicional

def generarPares(limite):

    num=1
    miLista=[]

    while num<limite:
        miLista.append(num*2)
        num=num+1

    return miLista

print(generarPares(10))

#generador

def generarPares2(limite):

    num2=1
 
    while num2<limite:
        yield num2*2 
        num2=num2+1

    
devuelvePares=generarPares2(10)



#Si queremos que lo imprima valor a valor

print(next(devuelvePares))

print("Aqui podria ir mas codigo")

print(next(devuelvePares)) 

print("Aqui podria ir mas codigo")

print(next(devuelvePares)) 

#si hicieramos un for, continuaria donde se quedo en el anterior, xq entra en
#estado de suspension entre llamada y llamada
for i in devuelvePares:
    print(i)