import random


class Personaje:

    def __init__(self, nombre, vida, ataque, defensa):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa

    def get_nombre(self):
        return self.nombre

    def get_vida(self):
        return self.vida

    def get_ataque(self):
        return self.ataque

    def get_defensa(self):
        return self.defensa

    def set_nombre(self, newnom):
        self.nombre = newnom

    def set_vida(self, newvid):
        self.vida = newvid

    def set_ataque(self, newata):
        self.ataque = newata

    def set_defensa(self, new_def):
        self.defensa = new_def

    def atacar_jugador(self, atacado,):
        defensa = random.randint(1, atacado.defensa)
        ataque = random.randint(1, self.ataque)

        if defensa < ataque:
            atacado.vida -= ataque - defensa
            print(
                f"Le has hecho {ataque - defensa} de daño a {atacado.nombre}")
            print(f"{atacado.nombre} te quedan {atacado.vida} de vida")
        else:
            print("No has hecho daño")

    def curar_jugador(self, numero_intentado):
        numero_adivinar = random.randint(1, 10)

        if numero_intentado == numero_adivinar:
            self.vida += numero_adivinar*3
            print(f"Acertaste te has curado {numero_adivinar * 3} de vida")
        else:
            print(
                f"Mala suerte el numero era {numero_adivinar} no te has curado")


def curar(jugador):

    numcurar = int(input(
        "Intenta adivinar el numero entre 1 y 10 para curar la cantidad del numero x3:\n"))
    jugador.curar_jugador(numcurar)


def jugar(jugador, atacado):

    print(f"{jugador.nombre}:{jugador.vida} de vida")
    opcion_jugador = input(f"{jugador.nombre} quieres atacar(A) o curar(C)?\n")

    if opcion_jugador == "A":
        print("Has atacado:")
        jugador.atacar_jugador(atacado)
    else:
        curar(jugador)

    print(" \n")


jugador1 = Personaje("Alan", 100, 30, 15)
jugador2 = Personaje("Alexa", 100, 30, 15)

print(f"{jugador1.nombre} empieza con {jugador1.vida} de vida")
print(f"{jugador2.nombre} empieza con {jugador2.vida} de vida")
print(" \n")

while jugador2.vida > 0 and jugador1.vida > 0:

    jugar(jugador2, jugador1)

    jugar(jugador1, jugador2)

if jugador1.vida > 0:
    print(f"{jugador1.nombre} gana")
    print(f"{jugador2.nombre} has muerto")
else:
    print(f"{jugador2.nombre} gana")
    print(f"{jugador1.nombre} has muerto")
