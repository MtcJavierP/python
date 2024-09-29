import sqlite3

# Crear la conexión

miConexion = sqlite3.connect("PrimeraBase")

#Para poder ejecutar sentencias SQL necesitamos un cursor o puntero

miCursor = miConexion.cursor()

#Crear una tabla
#OJO. LA GUARDA EN LA RAIZ DEL PROYECTO
#Y SOLO DEBE EJECUTARSE UNA VEZ,DESPUES DE EJECUTARLA UNA VEZ, COMENTARLA

#miCursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))")

#Insertar datos en la tabla

#miCursor.execute("INSERT INTO PRODUCTOS VALUES('BALÓN', 15, 'DEPORTES')")

#Probamos a usar una listas y tuplas para insertar varios registros

variosProductos = [
    ("Camiseta", 10, "Deportes"),
    ("Jarrón", 90, "Cerámica"),
    ("Camión", 20, "Juguetería")
]

#Existe un método llamado executemany que permite insertar varios registros a la vez
#en los values se pone tantos ? como campos tenga la tabla

#miCursor.executemany("INSERT INTO PRODUCTOS VALUES(?,?,?)", variosProductos)

#Leer datos de la tabla PRODUCTOS con el método SELECT

miCursor.execute("SELECT * FROM PRODUCTOS")

#Recuperar los datos de la consulta

variosProductos = miCursor.fetchall()

#Lo mostramos por pantalla

#print(variosProductos)

for producto in variosProductos:
    #print(producto)
    print("Nombre Artículo: ", producto[0], "Precio: ", producto[1], "Sección: ", producto[2])

#Guardar cambios, necesario despues de insertar datos

miConexion.commit()

#cerrar la conexión

miConexion.close()