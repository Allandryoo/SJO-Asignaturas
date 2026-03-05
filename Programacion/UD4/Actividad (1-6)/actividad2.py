class rectangulo:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura


base = int(input("Inidica la base\n"))
alturas = int(input("Indica la altura\n"))

area = rectangulo(base, alturas)

print("El area del rectangulo es " + str(area.calcular_area()))
