class Vehiculo:
    def __init__(self, ruedas, velocidad):
        self.ruedas = ruedas
        self.velocidad = velocidad


class Coche(Vehiculo):
    def __init__(self, ruedas, velocidad, puertas):
        super().__init__(ruedas, velocidad)
        self.puertas = puertas

    def getvelocidad(self):
        return self.velocidad

    def acelerar(self, newvel):
        self.velocidad = newvel


class Bicicleta(Vehiculo):
    def __init__(self, ruedas, velocidad, tipo):
        super().__init__(ruedas, velocidad)
        self.tipo = tipo

    def getvelocidad(self):
        return self.velocidad

    def acelerar(self, newvel):
        self.velocidad = newvel


coche1 = Coche(4, 10, 2)
bicicleta1 = Bicicleta(2, 5, "calle")

print(coche1.ruedas)
print(coche1.velocidad)
print(coche1.puertas)

print(bicicleta1.ruedas)
print(bicicleta1.velocidad)
print(bicicleta1.tipo)

coche1.acelerar(40)
print(coche1.velocidad)

bicicleta1.acelerar(15)
print(bicicleta1.velocidad)
