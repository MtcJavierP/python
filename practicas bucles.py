for letra in "Python":

    if letra=="h": #ignoraria la H y seguiria con las demas
        continue

    print("Viendo la letra: "+ letra)

nombre="Pildoras informaticas"

contador=0

for i in nombre:
   
    if i==" ":
        continue

    contador+=1

print(contador)

print(len(nombre))

#else

email=input("Introduce tu email")

for i in email:

    if i=="@":

        arroba=True

        break;

else: #forma parte del for y se ejecuta al acabar el for

    arroba=False

print(arroba)

#pass se usa en casos muy escasos, x ej cuando tenemos un  while true para romper 
# un bucle infinito o cuando dejamos trabajo para despues

while True:
    pass

class MiClase:
    pass #para implementar mas tarde

