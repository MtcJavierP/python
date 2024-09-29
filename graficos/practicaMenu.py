from tkinter import *
#hay que importar el modulo messagebox para poder mostrar mensajes emergentes
from tkinter import messagebox

root = Tk()
#creamos una funcion para mostrar un mensaje emergente
def infoAdicional():
    messagebox.showinfo("Procesador de Javi", "Procesador de texto version 2020")
#"Procesador de Javi" es el titulo de la ventana emergente y "Procesador de texto version 2020" es el mensaje que se muestra
#creamos una funcion para mostrar un mensaje de advertencia
def avisoLicencia():
    messagebox.showwarning("Licencia", "Producto bajo licencia GNU")

#creamos una funcion para salir de la aplicacion
def salirAplicacion():
    valor=messagebox.askquestion("Salir", "¿Deseas salir de la aplicacion?")
    if valor=="yes":
        root.destroy()
#Los valores que devuelve el messagebox.askquestion son "yes" o "no"
#si usaramos el messagebox.askokcancel los valores que devolveria serian "True" o "False"

#creamos una funcion para cerrar un documento
def cerrarDocumento():
    valor=messagebox.askretrycancel("Reintentar", "No es posible cerrar. Documento bloqueado")
    if valor==False:
        root.destroy()
#Los valores que devuelve el messagebox.askretrycancel son True o False

barraMenu=Menu(root)
root.config(menu=barraMenu,width=300, height=300)

#creamos los menus, el tearoff es para quitar la primera linea
archivoMenu=Menu(barraMenu, tearoff=0)

archivoEdicion=Menu(barraMenu, tearoff=0)

archivoHerramientas=Menu(barraMenu, tearoff=0)

archivoAyuda=Menu(barraMenu, tearoff=0)

#añadimos los menus a la barra de menu
barraMenu.add_cascade(label="Archivo", menu=archivoMenu)
barraMenu.add_cascade(label="Edicion", menu=archivoEdicion)
barraMenu.add_cascade(label="Herramientas", menu=archivoHerramientas)
barraMenu.add_cascade(label="Ayuda", menu=archivoAyuda)

#Creamos los submenus de archivo
archivoMenu.add_command(label="Nuevo")
archivoMenu.add_command(label="Abrir")
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Cerrar", command=cerrarDocumento)
archivoMenu.add_separator()
archivoMenu.add_command(label="Salir", command=salirAplicacion)


#Creamos los submenus de edicion
archivoEdicion.add_command(label="Copiar")
archivoEdicion.add_command(label="Cortar")
archivoEdicion.add_command(label="Pegar")

#Creamos los submenus de herramientas
archivoHerramientas.add_command(label="Herramienta 1")
archivoHerramientas.add_command(label="Herramienta 2")
archivoHerramientas.add_command(label="Herramienta 3")

#Creamos los submenus de ayuda
archivoAyuda.add_command(label="Licencia",command=avisoLicencia)
archivoAyuda.add_command(label="Acerca de...",command=infoAdicional)


root.mainloop()