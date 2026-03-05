class Animal:
    def __init__(self, mover):
        self.mover = mover


class Pajaro(Animal):
    def __init__(self, mover, volar):
        super().__init__(mover)
        self.volar = volar


class Pez(Animal):
    def __init__(self, mover, nadar):
        self.mover = mover
        self.nadar = nadar


pajaro1 = Pajaro("Saltar", "Empezar a volar")
pez1 = Pez("Mover cola", "Empezar a nadar")

print(pajaro1.mover)
print(pajaro1.volar)
print(pez1.mover)
print(pez1.nadar)
