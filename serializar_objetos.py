import pickle

#SERIALIZACION DE OBJETOS
#Creamos una clase vehiculos

class Vehiculos():

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.acelera = False
        self.frena = False

#metodos comunes a todos los vehiculos
    def arrancar(self):
        self.enmarcha = True

    def acelerar(self):
        self.acelera = True

    def frenar(self):
        self.frena = True

    def estado(self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ", self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena)


#Creamos 3 objetos de la clase Vehiculos

coche1 = Vehiculos("Mazda", "MX5")

coche2 = Vehiculos("Seat", "Leon")

coche3 = Vehiculos("Renault", "Megane")

#Creamos una lista o coleccion de objetos

coches=[coche1, coche2, coche3]

#Creamos un archivo externo, pero tiene q
#tener escritura binaria, eso se hace con "wb"

fichero = open("loscoches", "wb")

#volcamos la lista en el archivo

pickle.dump(coches, fichero)

#cerramos el archivo

fichero.close()

#borramos la lista

del(fichero)

#esto lo que hace es guardar la lista de objetos en un archivo
#externo, para poder recuperarla en otro momento


#RECUPERACION DE LA LISTA DE OBJETOS
#ahora vamos a recuperar la lista de objetos

ficheroApertura = open("loscoches", "rb")

#Creamos una variable que recupere la lista de objetos
#que hemos guardado en el archivo

misCoches = pickle.load(ficheroApertura)

#cerramos el archivo

ficheroApertura.close()

#recorremos la lista de objetos

for c in misCoches:

    print(c.estado())
