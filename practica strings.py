nombreUsuario = input("Introduce tu nombre de usuario: ")

edad = input("Introduce tu edad: ")

print("El nombre es: ", nombreUsuario.upper())
print("El nombre es: ", nombreUsuario.lower())
print("El nombre es: ", nombreUsuario.capitalize())
print("El nombre es: ", nombreUsuario.title())
print("El nombre es: ", nombreUsuario.replace("a", "e"))
print("El nombre es: ", nombreUsuario.replace("a", "e").upper())
print("El nombre es: ", nombreUsuario.replace("a", "e").lower())

print("La edad es: ", edad.isdigit()) #es boolean

while(edad.isdigit() == False):
    print("Introduce un valor numérico")
    edad = input("Introduce tu edad: ")


if(int(edad) < 18):
    print("No puedes pasar")
else:
    print("Puedes pasar")