class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


class Empleado(Persona):
    def __init__(self, nombre, edad, salario):
        super().__init__(nombre, edad)
        self.salario = salario

    def datos(self):
        return (f"{self.nombre}, {self.edad} años y cobra {self.salario}")


empleado1 = Empleado("Alan", 23, 50000)

print(empleado1.nombre)
print(empleado1.edad)
print(empleado1.salario)
print(empleado1.datos())
