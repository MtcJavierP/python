def suma(num1, num2):
	return num1+num2

def resta(num1, num2):
	return num1-num2

def multiplica(num1, num2):
	return num1*num2

def divide(num1,num2):
		
	try:
		return num1/num2
		
	except ZeroDivisionError:
		print("No se puede dividir entre cero")
		return "Operacion erronea"

#para solucionar  excepciones, tenemos q hacer una captura de los errores
# imaginemos el error de dividir por cero

 #try para q salte si no metemos entero

while True:
	try:
		op1=(int(input("Introduce el primer numero: ")))
		op2=(int(input("Introduce el segundo numero: ")))	
		break	
	
	except ValueError:
		print("Los valores no son correctos. Intenta de nuevo")

operacion=input("Introduce la operaci�n a realizar (suma,resta,multiplica,divide): ")

if operacion=="suma":
	print(suma(op1,op2))

elif operacion=="resta":
	print(resta(op1,op2))

elif operacion=="multiplica":
	print(multiplica(op1,op2))

elif operacion=="divide":
	print(divide(op1,op2))

else:
	print ("Operaci�n no contemplada")


print("Operaci�n ejecutada. Continuaci�n de ejec�ci�n del programa ")