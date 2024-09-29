def devuelve_ciudades(*ciudades): #con el * decimos q recibe un nº inde
#terminado de elementos, y en forma de tupla
    for elemento in ciudades: #bucle padre
        yield elemento

ciudades_devueltas=devuelve_ciudades("Madrid","Barcelona","Bilbao","Valencia")

print(next(ciudades_devueltas))

print(next(ciudades_devueltas))

#imaginemos q ahora queremos acceder a los subelementos de cada elemento
# en este caso, las letras

def devuelve_ciudades2(*ciudades): #con el * decimos q recibe un nº inde
#terminado de elementos, y en forma de tupla
    for elemento in ciudades: #bucle padre
        for subElemento in elemento: 
           yield subElemento
           

#Ahora lo mismo, pero usando el yield from
def devuelve_ciudades3(*ciudades): #con el * decimos q recibe un nº inde
#terminado de elementos, y en forma de tupla
    for elemento in ciudades: #bucle padre
      
           yield from elemento

