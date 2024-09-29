
class Persona():
    def __init__(self, nombre, edad, lugar_residencia):
        self.nombre = nombre
        self.edad = edad
        self.lugar_residencia = lugar_residencia

    def descripcion(self):
        print("Nombre:", self.nombre, "Edad:", self.edad, "Residencia:", self.lugar_residencia)


class Empleado(Persona):
    def __init__(self, salario, antiguedad, nombre_empleado, edad_empleado, residencia_empleado):
        super().__init__(nombre_empleado, edad_empleado, residencia_empleado)
        self.salario = salario
        self.antiguedad = antiguedad

    def descripcion(self):
        #llama al metodo descripcion de la clase padre
        super().descripcion()
        print("Salario:", self.salario, "Antiguedad:", self.antiguedad)       


Antonio = Persona("Antonio", 55,"España")
Antonio.descripcion()

Maria = Empleado(1500, 15,"Maria",40,"España")

Maria.descripcion()

print(isinstance(Antonio, Empleado))
print(isinstance(Maria, Persona))