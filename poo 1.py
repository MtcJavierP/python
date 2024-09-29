class Coche():

    def __init__(self): #Constructor, es el estado inicial de las propiedades de la clase
        
        self.__largoChasis=250
        self.__anchoChasis=120
        self.__ruedas=4
        self.__enmarcha=False

#usamos la encapsulacion, no se puede acceder a las propiedades 
# directamente, solo a traves de metodos, esto se hace poniendo __
# delante de la propiedad

   

    #Comportamiento, determinado por metodos

    def arrancar(self,arrancamos): #self es como el this de java
        self.__enmarcha=arrancamos

        if(self.__enmarcha):
            chequeo=self.__chequeo_interno()

        if(self.__enmarcha and chequeo):
            return "El coche esta en marcha"
        elif(self.__enmarcha and chequeo==False):
            return "Algo ha ido mal en el chequeo, no podemos arrancar"
        else:
            return "El coche esta parado"


    def estado(self):

        print("El coche tiene ", self.__ruedas," ruedas. Un ancho de ",self.__anchoChasis," y un largo de ",self.__largoChasis)

#Creamos una instancia de clase u objeto, no se usa new como en java

 #Creamos un metodo para probar la encapsulacion de metodos
#ponemos __ para que no se pueda acceder desde fuera de la clase
    def __chequeo_interno(self):
        print("Realizando chequeo interno")

        self.gasolina="ok"
        self.aceite="ok"
        self.puertas="cerradas"   

        if(self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="cerradas"): 
            return True

        else:
            return False


miCoche=Coche()

#Usamos el metodo
print(miCoche.arrancar(True))

miCoche.estado()

print("A continuacion creamos el segundo objeto-----------------")

miCoche2=Coche()

print(miCoche2.arrancar(False))
miCoche2.estado()