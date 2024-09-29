print("Programa de evaluacion de notas de alumnos")

#Funcion para meter el dato por teclado, devuelve string 
nota_alumno=input("Introduce la nota del alumno: ")

#Funcion para ejecutar el IF, este es el AMBITO de la variable valoracion
def evaluacion(nota) : 
    valoracion ="aprobado"
    if nota<5:
        valoracion="suspenso"
       
    return valoracion
    
#Aqui ejecutamos funcion y pasamos de stringn a int el valor del input
print(evaluacion(int(nota_alumno)))