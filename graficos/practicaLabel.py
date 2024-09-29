from tkinter import *

root = Tk()

miFrame = Frame(root, width=1200, height=600)

miFrame.pack()
#si quisieramos meter imagenes
miImagen = PhotoImage(file="lucha.png")
Label(miFrame, image=miImagen)


#Creamos la label
miLabel = Label(miFrame, text="Hola Alumnos de Python", fg="red", font=("Comic Sans MS", 18))
miLabel.place(x=100, y=200)



root.mainloop()