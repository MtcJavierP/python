import pickle

#Creamos una lista de nombres
lista_nombres = ["Pedro", "Ana", "María", "Isabel"]

#Creamos un archivo externo, pero tiene q 
#tener escritura binaria, eso se hace con "wb"

fichero_binario = open("lista_nombres", "wb")

#volcamos la lista en el archivo

pickle.dump(lista_nombres, fichero_binario)

#cerramos el archivo
fichero_binario.close()

#borramos la lista
del(fichero_binario)

#esto nos devuelve un archivo binario con la lista de nombres
#
#ahora vamos a recuperar la lista de nombres y leerla

