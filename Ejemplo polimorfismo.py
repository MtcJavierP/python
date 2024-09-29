class Coche():

    def desplazamiento(self):
        print("Me desplazo utilizando cuatro ruedas")

class Moto():
    
        def desplazamiento(self):
            print("Me desplazo utilizando dos ruedas")

class Camion():
        
            def desplazamiento(self):
                print("Me desplazo utilizando seis ruedas")


#Creamos un metodo que recibe un objeto por parametro
#Como python es un lenguaje dinamico, no importa el tipo de objeto que se pase
#siempre y cuando tenga el metodo desplazamiento
#ya que python no es fuertemente tipado

def desplazamientoVehiculo(vehiculo):
    vehiculo.desplazamiento()

#Creamos los objetos
miVehiculo = Moto()
desplazamientoVehiculo(miVehiculo)