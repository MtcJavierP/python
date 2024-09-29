for estaciones in ["primavera","verano","otoño","invierno"] :
    print(estaciones) #Lo printa tantas veces como elementos tiene la lista


for i in ["Pildoras","Informaticas",3] :
    print("Hola",end=" entre bucles ") #con el end "" hacemos que no haga salto de linea
    #Si le ponemos espacio en blanco pone los espacios, podemos poner lo q keramos

email=False
miEmail=input("Introduce tu direccion de email: ")
contador=0

for i in miEmail :
    #recorre tantas veces como caracteres tenga el string
    if(i=="@" or i=="."):
        email=True
        contador=contador+1

#cuando estamos analizando una booleana, no hace falta q pongamos el ==True
if contador==2:
    print("El mail es correcto")
else:
    print("El mail no es correcto")


#Tipo range, nos coge una especie de array con un rango

for i in range(5):
    print(f"Valor de la variable {i}") 
    #asi nos printa el texto con el valor de la variable a cada vuelta de bucle

for i in range(5,10):
    print(f"Valor de la variable {i}") 
    #asi nos printa el texto con el valor de la variable a cada vuelta de bucle

for i in range(5,50,3):
  #poniendo asi el range,empieza en el 5, acaba en el 50 y cuenta de 3 en 3
    print(f"Valor de la variable {i}") 
    #asi nos printa el texto con el valor de la variable a cada vuelta de bucle


valido=False
email2=input("Introduce tu email")

for i in range(len(email2)):
    if email2[i]=="@":
        valido=True

if valido:
    print("Email correcto")        
else:
    print("Email incorrecto")