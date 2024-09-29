from tkinter import *

raiz = Tk()

miFrame = Frame(raiz, width=1200, height=600)
miFrame.pack()

#para el button
miNombre = StringVar() #variable de control para el Entry

#para ubicar bien los elementos, lo mas aconsejable es usar grid(row=, column=)

nombreLabel = Label(miFrame, text="Nombre:")
nombreLabel.grid(row=0, column=0,sticky="e",padx=10,pady=10) #sticky="e" para alinear a la derecha

contraseñaLabel = Label(miFrame, text="Contraseña:")
contraseñaLabel.grid(row=1, column=0,sticky="e",padx=10,pady=10)

apellidoLabel = Label(miFrame, text="Apellido:")
apellidoLabel.grid(row=2, column=0,sticky="e",padx=10,pady=10)

direccionLabel = Label(miFrame, text="Dirección de casa:")
direccionLabel.grid(row=3, column=0,sticky="e",padx=10,pady=10)

cuadroNombre = Entry(miFrame,textvariable=miNombre)
#textvariable=miNombre para que el Entry tenga una variable de control
cuadroNombre.grid(row=0, column=1,padx=10,pady=10)
cuadroNombre.config(fg="red",justify="center") 
#color de la fuente y alineacion del texto

cuadroContraseña = Entry(miFrame)
cuadroContraseña.grid(row=1, column=1,padx=10,pady=10)
cuadroContraseña.config(show="*") #para que no se vea la contraseña

cuadroApellido = Entry(miFrame)
cuadroApellido.grid(row=2, column=1,padx=10,pady=10)

cuadroDireccion = Entry(miFrame)
cuadroDireccion.grid(row=3, column=1,padx=10,pady=10)

#probamos el button y el text

comentariosLabel = Label(miFrame, text="Comentarios:")
comentariosLabel.grid(row=4, column=0,sticky="e",padx=10,pady=10)

textoComentarios = Text(miFrame, width=16, height=5)
textoComentarios.grid(row=4, column=1,padx=10,pady=10)
#le añadimos un scroll
scrollVert = Scrollbar(miFrame, command=textoComentarios.yview)
#Lo colocamos a la derecha del texto en el grid, va en la columna 2
#con el sticky="nsew" se ajusta al tamaño del texto
scrollVert.grid(row=4, column=2, sticky="nsew")
#le decimos a la barra de scroll que se ajuste al texto
textoComentarios.config(yscrollcommand=scrollVert.set)


#Agregar un boton y q haga algo con command, q llame a la funcion
def codigoBoton():
    miNombre.set("Juan")

botonEnviar = Button(raiz, text="Enviar",command=codigoBoton)
botonEnviar.pack()

raiz.mainloop()
