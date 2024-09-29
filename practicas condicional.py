edad = 7

if 0<edad<100:
    print("La edad es correcta")
else:
    print("La edad es incorrecta")


#otro ejemplo

salarioPresidente=int(input("Introduce salario presidente "))
#para poder concatenar string con int hay q cambiar el tipo de dato
print("Salario presidente: " + str(salarioPresidente))

salarioDirector=int(input("Introduce salario director "))
print("Salario director: " + str(salarioDirector))

salarioJefeArea=int(input("Introduce salario del jefe de Area "))
print("Salario jefe de area: " + str(salarioJefeArea))

salarioAdministrativo=int(input("Introduce salario administrativo "))
print("Salario administrativo: " + str(salarioAdministrativo))


if salarioAdministrativo<salarioJefeArea<salarioDirector<salarioPresidente:
    print("Todo va OK")
else:
    print("Algo falla")

#EJEMPLO CON AND OR

print("Programa de becas del 2017")

distanciaEscuela=int(input("Introduce la distancia a la escuela en km: "))
print(distanciaEscuela)

numeroHermanos=int(input("Introduce el nº de hermanos en el centro: "))
print(numeroHermanos)

salarioFamiliar=int(input("Introduce el salario familiar: "))
print(salarioFamiliar)

if distanciaEscuela>40 and numeroHermanos>2 or salarioFamiliar<=20000:
    print("Tienes derecho a beca")
else:
    print("No tienes derecho")


#Ejemplo con IN

print("Asignaturas optativas año 2017")
print("Informatica Grafica - Pruebas de Software - Usabilidad y Accesibilidad")

opcion=input("Escribe la asignatura escogida: ")

asignatura=opcion.lower() #pasa lo que escribas a minusculas, para que coincida si o si
#ya que python es Case Sensitive
if asignatura in ("informatica grafica","pruebas de software","usabilidad y accesibilidad"):
    print("Asignatura elegida: " + asignatura)
else:
    print("La asignatura escogida no  está contemplada")
