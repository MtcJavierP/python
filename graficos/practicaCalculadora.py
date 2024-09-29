from tkinter import *

raiz = Tk()

miFrame = Frame(raiz, width=1200, height=600)

miFrame.pack()

operacion=""
resultado=0

#Primero configuramos la pantalla
numeroPantalla=StringVar()

pantalla=Entry(miFrame,textvariable=numeroPantalla)
#con colspan=4 hacemos que el campo de texto ocupe 4 columnas
pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4)
pantalla.config(bg="black", fg="#03f943", justify="right")

#-----------------PULSACIONESN TECLADO

def numeroPulsado(num):

    global operacion
    #si la operacion es distinta de vacio, es que se ha pulsado un operador
    #y hay que limpiar la pantalla
    if operacion!="":
        numeroPantalla.set(num)
        operacion=""
    else:
    #con get() obtenemos el valor que hay en la pantalla 
    #con set() establecemos el valor que queremos que haya en la pantalla
        numeroPantalla.set(numeroPantalla.get()+num)

#-----------------FUNCION SUMA

def suma(num):
    #guarda el valor que hay en la pantalla en la variable global resultado
    #y la operacion que se va a realizar
    global operacion
    global resultado
    resultado+=float(num)
    operacion="suma"
    #que vaya escribiendo en la pantalla el resultado
    numeroPantalla.set(resultado)
   
#-----------------FUNCION EL_RESULTADO

def el_resultado():
    global resultado
    #con eval() se evalua la operacion que hay en la pantalla
    #y se guarda en resultado
    numeroPantalla.set(resultado+float(numeroPantalla.get()))
    #reseteamos el resultado
    resultado=0

#Luego configuramos los botones
#---------------FILA 1
#Boton 7
boton7=Button(miFrame, text="7", width=3,command=lambda:numeroPulsado("7"))
boton7.grid(row=2, column=1)
#Boton 8
boton8=Button(miFrame, text="8", width=3,command=lambda:numeroPulsado("8"))
boton8.grid(row=2, column=2)
#Boton 9
boton9=Button(miFrame, text="9", width=3,command=lambda:numeroPulsado("9"))
boton9.grid(row=2, column=3)
#Boton /
botonDiv=Button(miFrame, text="/", width=3)
botonDiv.grid(row=2, column=4)
#---------------FILA2
#Boton 4, si lo ponemos asi, no funciona, porque se ejecuta la
# funcion al cargar el programa
#boton4=Button(miFrame, text="4", width=3,command=numeroPulsado("4"))
#para que funcione, debemos hacerlo asi, con una funcion lambda

boton4=Button(miFrame, text="4", width=3,command=lambda:numeroPulsado("4"))
boton4.grid(row=3, column=1)
#Boton 5
boton5=Button(miFrame, text="5", width=3,command=lambda:numeroPulsado("5"))
boton5.grid(row=3, column=2)
#Boton 6
boton6=Button(miFrame, text="6", width=3,command=lambda:numeroPulsado("6"))
boton6.grid(row=3, column=3)
#Boton *
botonMult=Button(miFrame, text="*", width=3)
botonMult.grid(row=3, column=4)
#---------------FILA 3
#Boton 1
boton1=Button(miFrame, text="1", width=3,command=lambda:numeroPulsado("1"))
boton1.grid(row=4, column=1)
#Boton 2
boton2=Button(miFrame, text="2", width=3,command=lambda:numeroPulsado("2"))
boton2.grid(row=4, column=2)
#Boton 3
boton3=Button(miFrame, text="3", width=3,command=lambda:numeroPulsado("3"))
boton3.grid(row=4, column=3)
#Boton -
botonRest=Button(miFrame, text="-", width=3)
botonRest.grid(row=4, column=4)
#---------------FILA 4
#Boton 0
boton0=Button(miFrame, text="0", width=3,command=lambda:numeroPulsado("0"))
boton0.grid(row=5, column=1)
#Boton .
botonComa=Button(miFrame, text=",", width=3,command=lambda:numeroPulsado(","))
botonComa.grid(row=5, column=2)
#Boton =
botonIgual=Button(miFrame, text="=", width=3,command=lambda:el_resultado())
botonIgual.grid(row=5, column=3)
#Boton +
botonSum=Button(miFrame, text="+", width=3,command=lambda:suma(numeroPantalla.get()))
botonSum.grid(row=5, column=4)




raiz.mainloop()