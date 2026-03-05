import random
limitx=10
limity=10
class Persona:
    def __init__(self, nombre, resistencia, altura, posx, posy):
        self.nombre = nombre
        self.resistencia = resistencia
        self.altura = altura
        self.posx = posx 
        self.posy = posy

    def mostrar_posicion(self):
        print(f"Posicion actual:({self.posx}, {self.posy})")
        print(f"Resistencia:{self.resistencia}")
        if self.posx == 0 and self.posy == 0:
            self.resistencia = self.resistencia + 10
            print("Has recuperado la resistencia")
            print(self.resistencia)

        for p in pociones:
            if p.misma_posicion(self):
                p.posx=-1
                p.posy=-1
                self.resistencia=self.resistencia+10
                pociones.remove(p)
                print(pociones)


    def usar_pocion(self, pocionpos):
        if self.posx == pocionpos.posx and self.posy == pocionpos.posy:
            print("Has encontrado un pocion recuperas 10 de resistencia")
            self.resistencia += 10

    def encontrar_dracula(self, dracula):
        if persona1.posx == dracula.posx and persona1.posy == dracula.posy:
            print(f"Te has encontrado a {dracula.nombre} pierdes 5 de energia")
            self.resistencia -= 5

    def arriba(self):
        if self.posy < limity:
            self.posy = self.posy + 1
            self.resistencia = self.resistencia - 1
        else:
            print("Te vas a caer del mapa")
        self.mostrar_posicion()

    def abajo(self):
        if self.posy > 0:
            self.posy = self.posy - 1
            self.resistencia = self.resistencia - 1
        else:
            print("Te vas a caer del mapa")
        self.mostrar_posicion()

    def izquierda(self):
        if self.posx > 0:
            self.posx = self.posx - 1
            self.resistencia = self.resistencia - 1
        else:
            print("Te vas a caer del mapa")
        self.mostrar_posicion()

    def derecha(self):
        if self.posx < limitx:
            self.posx = self.posx + 1
            self.resistencia = self.resistencia - 1
        else:
            print("Te vas a caer del mapa")
        self.mostrar_posicion()

    def teletransporte(self):
        x = int(input("Posicion X: "))
        y = int(input("Posicion Y: "))
        if x >= 0 and x <= limitx and y >= 0 and y <= limity:
            self.posx = x
            self.posy = y
            self.resistencia = self.resistencia - 5
        else:
            print("No puedo moverme")
        self.mostrar_posicion()

class Pocion:
    def __init__(self, nombre):
        self.nombre = nombre
        self.posx = random.randint(0,5)
        self.posy = random.randint(0,5)
        print(f"Posicion de la pocion: X{self.posx} y{self.posy}")

    def misma_posicion(self, persona):
        if self.posx == persona.posx and self.posy == persona.posy:
            print(f"Has obtenido la pocion {self.nombre}")
            return True

aleatoriox = random.randint(0,5)
aleatorioy = random.randint(0,5)

persona1 = Persona("Alan", 100, 1.85, 0, 0)
print(f"Posicion actual:({persona1.posx}, {persona1.posy})")

dracula = Persona("Ionut", 10, 1.70, aleatoriox, aleatorioy)
print(dracula.posx,dracula.posy)

p1 = Pocion("Platano")
p2 = Pocion("Manzana")
p3 = Pocion("Kiwi")

pociones=[p1,p2,p3]

while persona1.resistencia > 0:
    
    persona1.encontrar_dracula(dracula)

    opcion = input("A donde quieres ir?\n")

    match opcion:

        case "w":
            persona1.arriba()

        case "s":
            persona1.abajo()

        case "a":
            persona1.izquierda()

        case "d":
            persona1.derecha()

        case "goku":
            persona1.teletransporte()

        case _:
            print("Has salido del juego")
            break
print("Te has quedado sin resistencia")