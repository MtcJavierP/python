def divide():

    try:
        op1=(float(input("Introduce el primer nº")))
        op2=(float(input("Introduce el segundo nº")))

        print("La division es: "+ str(op1/op2))
    except:
        print("Valor incorrecto")
    except ZeroDivisionError:
        print("No entre cero")
    except: #esto se usa para q recoja cualquier error
        print("Ha ocurrido un error")    

    finally: #este codigo se ejecuta siempre,solo si hay except
        print("Calculo finalizado")

divide()