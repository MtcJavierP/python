#Clase padre o superclase
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


#Creamos la clase furgo que hereda de vehiculos

class Furgoneta(Vehiculos):
    def carga(self, cargar):
        self.cargado = cargar
        if (self.cargado==True):
            return "La furgoneta está cargada"
        else:
            return "La furgoneta no está cargada"

#Clase que hereda de Vehiculos
class Moto(Vehiculos):
    #creamos un comportamiento exclusivo para motos
    hcaballito = ""

    def caballito(self):
        self.hcaballito = "Voy haciendo el caballito"
#Sobreescribimos el metodo estado
    def estado(self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ", self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena,"\n", self.hcaballito)


#Creamos la clase vehiculo electrico

class VElectricos(Vehiculos):
    def __init__(self, marca, modelo):
        #la funcion super() llama al constructor de la clase padre
        super().__init__(marca, modelo)
        self.autonomia = 100

    def cargarEnergia(self):
        self.cargando = True

#Usamos la herencia multiple, heredando de dos clases
#se da preferencia a la primera clase que se pone en la herencia
class BicicletaElectrica(VElectricos, Vehiculos):
    pass
    #hereda todos los metodos y propiedades de las dos clases

