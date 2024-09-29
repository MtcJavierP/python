from tkinter import *

root = Tk()

root.title("Ejemplo")

playa=IntVar()
montagna=IntVar()
turismoRural=IntVar()

#añadimos funcionalidad a los checkbuttons
def opcionesViaje():
    opcionEscogida=""
    if(playa.get()==1):
        opcionEscogida+="Playa"
    if(montagna.get()==1):
        opcionEscogida+="Montaña"
    if(turismoRural.get()==1):
        opcionEscogida+="Turismo Rural"
    textoFinal.config(text=opcionEscogida)

foto=PhotoImage(file=r"D:\proyectosgit\python\graficos\avion.png", width=100, height=100)
Label(root, image=foto).pack()

frame=Frame(root)
frame.pack()

Label(frame, text="Elige destinos", width=50).pack()
#variable la igualamos as la q esta en la funcion, el onvalue 
# es el valor q se le asigna a la variable si esta seleccionado
Checkbutton(root, text="Playa",variable=playa,onvalue=1,command=opcionesViaje).pack()
Checkbutton(root, text="Montaña",variable=montagna,onvalue=1,command=opcionesViaje).pack()
Checkbutton(root, text="Turismo Rural",variable=turismoRural,onvalue=1,command=opcionesViaje).pack()

textoFinal=Label(frame)
textoFinal.pack()

root.mainloop()