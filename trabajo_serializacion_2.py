import pickle

#Abrimos el archivo en modo lectura binaria
fichero = open("lista_nombres", "rb")

#Cargamos la lista de nombres
lista = pickle.load(fichero)

#Mostramos la lista
print(lista)


