class Persona:
    def __init__(self, nombre, apellidos, edad, sexo):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad
        self.sexo = sexo

    def presentar(self):
        return "Hola soy " + self.nombre + " " + self.apellidos + " y tengo " + str(self.edad) + " años"


persona1 = Persona("alan", "santos", 21, "M")
persona2 = Persona("good", "boy", 18, "F")

print(persona1.presentar())
