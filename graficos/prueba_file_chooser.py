from tkinter import *
from tkinter import filedialog

root = Tk()

def abrirFichero():
  # filedialog.askopenfilename() devuelve el nombre del archivo seleccionado  
    root.filename = filedialog.askopenfilename(title="Selecciona un archivo",initialdir="C:", filetypes=(("Ficheros de texto", "*.txt"), ("Todos los ficheros", "*.*")))
    print(root.filename)#nos muestra la ruta del archivo seleccionado

    #ESTO LO PROPUSO COPILOT
    # #abrimos el archivo seleccionado en modo lectura
    # archivo=open(root.filename, "r")
    # #leemos el archivo
    # contenido=archivo.read()
    # #cerramos el archivo
    # archivo.close()
    # #mostramos el contenido del archivo
    # print(contenido)
    # #creamos una ventana emergente con el contenido del archivo
    # messagebox.showinfo("Contenido del archivo", contenido)
    # #mostramos el contenido del archivo en un cuadro de texto
    # texto=Text(root, width=50, height=10)
    # texto.pack()
    # texto.insert(1.0, contenido)
    # texto.config(state=DISABLED)#el texto no se puede modificar
    # #mostramos el contenido del archivo en un cuadro de texto con scroll
    # scroll=Scrollbar(root, command=texto.yview)
    # scroll.pack(side="right", fill="y")
    # texto.config(yscrollcommand=scroll.set)
    # texto.insert(1.0, contenido)
    # texto.config(state=DISABLED)#el texto no se puede modificar



Button(root, text="Abrir fichero", command=abrirFichero).pack()



root.mainloop()
