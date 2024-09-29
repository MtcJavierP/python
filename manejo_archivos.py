from io import open


archivo_texto=open("archivo.txt","r")

#print(archivo_texto.read())

#ponemos el puntero en la posicion 11
#archivo_texto.seek(11)
#printamos el contenido desde la posicion 11
#print(archivo_texto.read())

#tambien podemos hacer que lea hasta el caracter que queramos con el read
#print(archivo_texto.read(11))
#leer desde la posicion 0 hasta la mitad del archivo
#archivo_texto.seek(len(archivo_texto.read())/2)

#print(archivo_texto.read())

#que lea despues de la primera linea

#archivo_texto.seek(len(archivo_texto.readline()))
#print(archivo_texto.read())

#si queremos tanto leer como escribir en un archivo

archivo_texto=open("archivo.txt","r+") #asi es lectura y escritura

#asi lo escribe en la primera linea
#archivo_texto.write("Comienzo del texto")

#si queremos escribir en una posicion especifica

lineas_texto=archivo_texto.readlines()

lineas_texto[1]="Esta linea ha sido incluida desde el exterior\n"
#llevamos el puntero al principio
archivo_texto.seek(0)

archivo_texto.writelines(lineas_texto)
archivo_texto.close()
