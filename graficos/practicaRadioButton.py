from tkinter import *

root = Tk()

varOpcion = IntVar()

Label(root, text="Género:").pack()

#Para rescatar el valor de un radiobutton, se hace con get()

def imprimir():
   # print(varOpcion.get())
    if(varOpcion.get()==1):
        etiqueta.config(text="Has elegido Masculino")
    elif(varOpcion.get()==2):
        etiqueta.config(text="has elegido Femenino")
    else:
        etiqueta.config(text="Has elegido Otra opción")
#con variable=varOpcion, se asocia el radiobutton a la variable varOpcion
#con value=1, se le asigna un valor a cada radiobutton
Radiobutton(root, text="Masculino", variable=varOpcion,value=1,command=imprimir).pack()

Radiobutton(root, text="Femenino",variable=varOpcion, value=2,command=imprimir).pack()

Radiobutton(root, text="Femenino",variable=varOpcion, value=3,command=imprimir).pack()

etiqueta=Label(root)
etiqueta.pack()



root.mainloop()