miDiccionario={"Alemania":"Berlin","Francia":"Paris","Reino Unido":"Londres","España":"Madrid"}

#Para poder acceder al valor, tenemos que dar la clave
print(miDiccionario["Francia"])

#agregar elemento
miDiccionario["Italia"]="Lisboa"
print(miDiccionario)
#Sobreescribir un valor erroneo
miDiccionario["Italia"]="Roma"
print(miDiccionario)

#Eliminar elementos
del miDiccionario["Reino Unido"]

#Diccionario con mezcla de tipos
miDiccionario2 ={"Alemania":"Berlin", 23:"Jordan","Mosqueteros":3}

#Usar tupla para agregar claves a valores
miTupla=["España","Francia","Reino Unido","Alemania"]
miDiccionario3={miTupla[0]:"Madrid",miTupla[1]:"Paris",miTupla[2]:"Londres",miTupla[3]:"Berlin"}
print(miDiccionario3["Francia"])

#Como hacer que un diccionario almacene una tupla entera de valores
miDiccionario4={23:"Jordan","Nombre":"Michael","Equipo":"Chicago","anillos":[1991,1992,1993,1997,1998]}
print(miDiccionario4)
print(miDiccionario4["Equipo"])
print(miDiccionario4["anillos"])

#Guardar un diccionario dentro de otro diccionario
miDiccionario5={23:"Jordan","Nombre":"Michael","Equipo":"Chicago","anillos":{"Temporadas":[1991,1992,1993,1997,1998]}}
print(miDiccionario5)
print(miDiccionario5["Equipo"])
print(miDiccionario5["anillos"])

#Metodos 
print(miDiccionario5.keys()) #imprime claves
print(miDiccionario5.values()) #imprime valores
print(len(miDiccionario5)) #longitud
