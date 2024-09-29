from tkinter import *

# Crear la ventana
raiz = Tk()

raiz.title("Ventana de pruebas")


# Tamaño de la ventana y que no se pueda modificar

raiz.resizable(1,1) #ancho (width), alto(height) 

#Cambiar el icono de la ventana
#necesitamos tener un archivo .ico
#r indica que es una ruta cruda
raiz.iconbitmap(r"D:\proyectosgit\python\graficos\lucha.ico")

#cambiar el tamaño por defecto

raiz.geometry("650x350")

#este metodo permite cambiar el color de fondo de la ventana y
#acepta colores en formato hexadecimal
raiz.config(bg="blue")

#para que nos abra la ventana directamente sin abrir la terminal
#tenemos que cambiar la extension py por pyw

#Creamos una nueva frame y la metemos dentro de la anterior

miFrame = Frame()
#con esto al ampliar el frame raiz el hijo miFrame se queda
#en la parte de abajo y a la izquierda
#miFrame.pack(side="bottom", anchor="n")
miFrame.pack(fill="x") #rellena el frame en el eje x
#le damos color y tamaño para visualizarla
miFrame.config(width="650", height="350")
miFrame.config(bg="red")

#cambiar borde
miFrame.config(bd=35)
miFrame.config(relief="groove")

#para cambiar el cursor del ratón

miFrame.config(cursor="pirate")
#todo lo q hemos aplicado a miFrame se lo podemos aplicar a raiz

#con mainloop se mantiene la ventana abierta
#mainloop debe ser la última línea de código
raiz.mainloop()