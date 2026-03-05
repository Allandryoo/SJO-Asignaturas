pi = 3.14


class circulo:

    def __init__(self, radios):
        self.radio = radios

    def calcular_area(self):
        return pi * (self.radio**2)

    def calcular_perimetro(self):
        return pi * (self.radio*2)


num = int(input("Indica el radio"))

radio = circulo(num)

print(radio.calcular_area())
print(radio.calcular_perimetro())
