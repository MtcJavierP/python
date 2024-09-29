def evaluaEdad(edad):
    
        if edad<0:
            raise MiPropioError("La edad debe ser mayor que cero")

        elif edad<20:
            return "Eres muy joven"
        elif edad<40:
            return "Eres joven"
        elif edad<65:
            return "Eres maduro"
        elif edad<100:
            return "Cuidate..."

print(evaluaEdad(80))

#Creamos nuestra propia excepcion

import math

def calculaRaiz(num1):
    if num1 <0:
        raise ValueError("El numero no puede ser negativo")
    else:
        return math.sqrt(num1)


op1= (int(input("Introduce un numero")))

try:
    print(calculaRaiz(op1))
except ValueError as ErrorDeNumeroNegativo:
    print(ErrorDeNumeroNegativo) 
    
print("Programa terminado")