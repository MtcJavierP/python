import math


i=1

while i<=10:
    print(f"Contando {i}")
    i+=1
    
print("Terminada ejecucion")

#Probamos un programa para introducir la edad

edad=int(input("Introduce la edad: "))

while edad<0 or edad>100:
    print("Edad incorrecta")
    edad=int(input("Introduce la edad: "))

print(f"Edad del aspirante: {edad}")

print ("Programa de calculo de raiz cuadrada")
numero= int(input("Introduce un nº por favor: "))

intentos=0

while numero<0:
    print("No se puede hayar la raiz de un negativo")

    if intentos==2:
        print("Has consumido demasiados intentos. El programa ha finalizado")
        break
    
    numero= int(input("Introduce un nº por favor"))
    if numero<0:
        intentos=intentos+1

if intentos<2:
    solucion=math.sqrt(numero)
    print("La raiz cuadrada de "+str(numero)+"es "+ str(solucion))
