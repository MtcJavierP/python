print("Verificacion de acceso")

edadUsuario=int(input("Introduce edad por favor: "))

if edadUsuario<18:
    print("No puede pasar")
 #if edadUsuario>100:     SI hicieramos asi daria error, porque el else
 # en python solo puede ir con un if, y coge el mas cercano, por lo q hacemos elif
elif edadUsuario>100:
        print("Edad incorrecta")
else:
    print("Puede pasar")

print("El programa ha finalizado")


#para poder agregar varias condiciones, ponemos elif


print("Verificacion de notas")

notaAlumno=int(input("Introduce nota por favor: "))

if notaAlumno<5:
    print("Insuficiente")

elif notaAlumno<6:
        print("suficiente")
elif notaAlumno<7:
        print("Bien")
elif notaAlumno<9:
        print("Notable")
elif notaAlumno>10:
        print("Nota incorrecta")
else:
    print("Sobresaliente")

print("El programa ha finalizado")
