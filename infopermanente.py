import pickle

class Persona:

    def __init__(self, nombre, genero, edad):
        self.nombre = nombre
        self.genero = genero
        self.edad = edad
        print("Se ha creado una persona nueva con el nombre de ", self.nombre)

#esto convierte en cadena de texto la informacion de un objeto

    def __str__(self):
        return "{} {} {}".format(self.nombre, self.genero, self.edad)


#creamos una lista de objetos de la clase persona

class ListaPersonas:

    personas = []

#Creamos un constructor para guardar la lista de personas
    def __init__(self):
        #abrimos el fichero en modo lectura binaria
        listaDePersonas=open("ficheroExterno", "ab+")
        #despues de agregar un objeto a la lista, 
        # el puntero se queda al final, x lo q lo pasamos al ppio
        listaDePersonas.seek(0)

        try:
            #cargamos la lista de personas del fichero
            self.personas = pickle.load(listaDePersonas)
            print("Se cargaron {} personas del fichero externo".format(len(self.personas)))
        except:
            print("El fichero esta vacio")
        finally:
            listaDePersonas.close()
            del(listaDePersonas)

    #Creamos dos metodos, uno para agregar personas a la lista y otro para mostrarlas

    def agregarPersonas(self, p):
        self.personas.append(p)
        #guardamos la lista de personas en el fichero
        self.guardarPersonasEnFicheroExterno()

    def mostrarPersonas(self):
        for p in self.personas:
            print(p)

    #Creamos un metodo para guardar la lista de personas en un fichero externo

    def guardarPersonasEnFicheroExterno(self):
        #abrimos el fichero en modo escritura binaria
        listaDePersonas=open("ficheroExterno", "wb")
        #guardamos la lista de personas en el fichero
        pickle.dump(self.personas, listaDePersonas)
        #cerramos el fichero
        listaDePersonas.close()
        #borramos la variable
        del(listaDePersonas)

    #Creamos un metodo para mostrar la informacion del fichero externo
    def mostrarInfoFicheroExterno(self):
        print("La informacion del fichero externo es la siguiente: ")
        for p in self.personas:
            print(p)


#Creamos una instancia de ListaPersonas
miLista=ListaPersonas()
#Creamos una instancia de Persona
persona=Persona("Ana", "Femenino", 19)
#Agregamos la persona a la lista
miLista.agregarPersonas(persona)
#Mostramos la informacion de la lista
miLista.mostrarInfoFicheroExterno()