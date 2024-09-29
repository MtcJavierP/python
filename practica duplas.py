miTupla=("Juan", 13,1,1995)
#Se puede crear sin los parentesis, esto se llama empaquetar tupla

print(miTupla[2])
#Convertir tupla a lista
miLista=list(miTupla)

#Convertir tupla en lista
miTupla2=tuple(miLista)

#saber si hay un elemento en la tupla
print("Juan" in miTupla)

#Saber cuantos elementos que le preguntemos se encuentran en la tupla-> count
print(miTupla.count(13))

#Saber la longitud de la tupla -> len
print(len(miTupla))

#Crear toplas de un elemento solo, poner coma al final
miTupla3=("Juan",)

#Desempaquetar una tupla, nos permite asignar todos los elementos
#de una tupla a variables, pero tienen q asignarse todos los elementos
# de la dupla

nombre, dia, mes, agno=miTupla
print(nombre)
print(agno)
print(dia)
print(mes)
