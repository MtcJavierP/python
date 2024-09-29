miLista=["Maria","Pepe",5,"Antonio"]

print(miLista[:]) #Imprime toda la lista
print(miLista[2]) #Imprime el q esta en la posicion 2
print(miLista[1:3]) #incluye los indices del 1 al 2
#, el primero es inclusive y el segundo excluye
print(miLista[:3]) #incluye los indices del 0 al 2 de forma mas abreviada, 
print(miLista[2:]) #incluye los indices del 2 al ultimo

# para agregar elementos a la lista
miLista.append("Sandra")

#Agregar un elemento en el punto que queramos
miLista.insert(2,"Tania")
#Añadir varios elementos
miLista.extend(["Ana","Lucia","Javi"])

#Si necesitamos saber el indice de un elemento
print(miLista.index("Ana"))

#Para saber si un elemento se encuentra en una lista
print( "Pepe" in miLista)

#Eliminar elementos de una lista
miLista.remove("Ana")

#Eliminar el ultimo elemento de la lista
miLista.pop()

#Sumar listas
miLista2=["Sandra","Lucia",7]
miLista3=miLista+miLista2

#Si queremos repetir la lista varias veces, multiplicamos
miLista*3
