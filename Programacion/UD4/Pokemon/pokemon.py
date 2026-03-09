import random

class Pokemon:
    def __init__(self, nombre, tipo, ataque, defensa):
        self.nombre = nombre
        self.tipo = tipo
        self.ataque = ataque
        self.defensa = defensa
        self.ps = 100
        self.psactual = self.ps
        self.psmax = self.ps

    def get_nombre(self):
        return self.nombre

    def get_tipo(self):
        return self.tipo

    def get_ataque(self):
        return self.ataque

    def get_defensa(self):
        return self.defensa

    def get_ps(self):
        return self.ps

    def set_ps(self, newps):
        self.ps = newps

    def mostrar_info(self):
        return f"Nombre: {self.nombre} | Tipo: {self.tipo} | ATK: {self.ataque} | DEF: {self.defensa} | PS: {self.ps}"


class PokemonPlanta(Pokemon):
    def __init__(self, nombre, tipo, ataque, defensa):
        super().__init__(nombre, tipo, ataque, defensa)
        self.tipo = "Planta"

    def ataque_especial(self):
        atkesp = self.ataque * 1.5
        return atkesp

    def elemento(self):
        print("debil contra fuego y fuerte contra agua\n")


class PokemonAgua(Pokemon):
    def __init__(self, nombre, tipo, ataque, defensa):
        super().__init__(nombre, tipo, ataque, defensa)
        self.tipo = "Agua"

    def ataque_especial(self):
        atkesp = self.ataque * 1.5
        return atkesp

    def elemento(self):
        print("debil contra planta y fuerte contra fuego\n")


class PokemonFuego(Pokemon):
    def __init__(self, nombre, tipo, ataque, defensa):
        super().__init__(nombre, tipo, ataque, defensa)
        self.tipo = "Fuego"

    def ataque_especial(self):
        atkesp = self.ataque * 1.5
        return atkesp

    def elemento(self):
        print("debil contra agua y fuerte contra planta\n")


class PokemonVolador(Pokemon):
    def __init__(self, nombre, tipo, ataque, defensa):
        super().__init__(nombre, tipo, ataque, defensa)
        self.tipo = "Volador"

    def ataque_especial(self):
        atkesp = self.ataque * 1.5
        return atkesp

    def elemento(self):
        print("debil contra roca y fuerte contra planta\n")


class Mapa:
    def __init__(self, lado):
        self.lado = lado
        self.mapa = []

    def Set_lado(self, newlado):
        self.lado = newlado

    def generar_mapa(self):
        for y in range(1, self.lado+1):
            for x in range(1, self.lado+1):
                self.mapa.append([None, (x, y)])

    def mostrar_mapa(self):
        linea = ""
        for i in self.mapa:
            if i[0] == None:
                linea += str(f"[Ninguno ,{i[1]}]")
            else:
                linea += str(f"[{i[0].get_nombre()},{i[1]}]")
            if i[1][0] == self.lado:
                print(linea)
                linea = ""

    def pokemon_mapa(self, pokemon, x, y):
        for i in self.mapa:
            if i[1][0] == x and i[1][1] == y:
                if i[0] == None:
                    i[0] = pokemon

    def añadir_pokemons(self):
        for i in self.mapa:
            if i[0] == None and random.randint(0, 1) == random.randint(0, 1):
                if i[1][0] == 1 and i[1][1] == 1:
                    i[0] = None
                else:
                    i[0] = almacen[random.randint(0, len(almacen)-1)]

    def hay_pokemon(self):
        comprobar = [none for none in self.mapa if none[0] != None]
        return comprobar


class Personaje:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def mover_izquierda(self):
        self.x -= 1

    def mover_derecha(self):
        self.x += 1

    def mover_arriba(self):
        self.y += 1

    def mover_abajo(self):
        self.y -= 1


class Jugador(Personaje):
    def __init__(self, x, y, nombre):
        super().__init__(x, y)
        self.nombre = nombre
        self.inventario = []

    def capturar_pokemon(self, pokemon, psactual, psmax):
        if psactual <= (psmax * 0.25):
            probabilidad_captura = 100
            print(f"Probabilidad de captura {probabilidad_captura}")
        elif psactual <= (psmax * 0.50):
            probabilidad_captura = 70
            print(f"Probabilidad de captura {probabilidad_captura}")
        elif psactual <= (psmax * 0.75):
            probabilidad_captura = 50
            print(f"Probabilidad de captura {probabilidad_captura}")
        else:
            probabilidad_captura = 30
            print(f"Probabilidad de captura {probabilidad_captura}")

        exito_captura = random.randint(0, 100)

        if probabilidad_captura >= exito_captura:
            p1.inventario.append(pokemon)
            print(
                f"{pokemon.get_nombre()} ha sido capturado y se ha añadido a tu inventario")
            return True
        else:
            print(f"{pokemon.get_nombre()} ha escapado")
            return False

    def llamar_pokemon(self):
        numero_random = random.randint(0, len(almacen)-1)

        self.inventario.append(almacen[numero_random])
        almacen.pop(numero_random)


def procesar_linea(linea):
    campos = []
    actual = ""

    for c in linea:
        if c == ",":
            campos.append(actual)
            actual = ""
        else:
            actual += c

    campos.append(actual)

    nombre = campos[0]
    tipo = campos[1].lower()
    ataque = int(campos[2])
    defensa = int(campos[3])

    match tipo:
        case "planta":
            return PokemonPlanta(nombre, tipo, ataque, defensa)
        case "agua":
            return PokemonAgua(nombre, tipo, ataque, defensa)
        case "fuego":
            return PokemonFuego(nombre, tipo, ataque, defensa)
        case "volador":
            return PokemonVolador(nombre, tipo, ataque, defensa)


def escoger_pokemon():
    print("Escoge un pokemon\n")
    for indice, valor in enumerate(p1.inventario):
        print(f"{indice}: {valor.mostrar_info()}")

    num_pokemon = int(
        input("Indica el numero del pokemon para seleccionarlo\n"))
    return num_pokemon


def combate_pokemon(mipokemon, pokemonsalvaje):

    miataque = mipokemon.get_ataque()
    mipsactual = mipokemon.get_ps()
    mipsmax = mipokemon.get_ps()
    midef = mipokemon.get_defensa()
    enemyataque = pokemonsalvaje.get_ataque()
    enemypsmax = pokemonsalvaje.get_ps()
    enemypsactual = pokemonsalvaje.get_ps()
    enemydef = pokemonsalvaje.get_defensa()

    if mipokemon.tipo == "Planta" and pokemonsalvaje.tipo == "Agua":
        miataque = mipokemon.ataque_especial()
        enemyataque = enemyataque / 1.5

    elif mipokemon.tipo == "Fuego" and pokemonsalvaje.tipo == "Planta":
        miataque = mipokemon.ataque_especial()
        enemyataque = enemyataque / 1.5

    elif mipokemon.tipo == "Agua" and pokemonsalvaje.tipo == "Fuego":
        miataque = mipokemon.ataque_especial()
        enemyataque = enemyataque / 1.5

    elif mipokemon.tipo == "Volador" and pokemonsalvaje.tipo == "Planta":
        miataque = mipokemon.ataque_especial()
        enemyataque = enemyataque / 1.5

    elif pokemonsalvaje.tipo == "Planta" and mipokemon.tipo == "Agua":
        miataque = miataque / 1.5
        enemyataque = pokemonsalvaje.ataque_especial()

    elif pokemonsalvaje.tipo == "Fuego" and mipokemon.tipo == "Planta":
        miataque = miataque / 1.5
        enemyataque = pokemonsalvaje.ataque_especial()

    elif pokemonsalvaje.tipo == "Agua" and mipokemon.tipo == "Fuego":
        miataque = miataque / 1.5
        enemyataque = pokemonsalvaje.ataque_especial()

    elif pokemonsalvaje.tipo == "Volador" and mipokemon.tipo == "Planta":
        miataque = miataque / 1.5
        enemyataque = pokemonsalvaje.ataque_especial()

    while True:

        print(f"{mipokemon.get_nombre()} salud:{mipsactual} | | {pokemonsalvaje.get_nombre()} salud:{enemypsactual}")
        print(
            f"ATK: {miataque} | DEF: {midef} | | ATK: {enemyataque} | DEF: {enemydef}")

        print(f"Turno de {p1.nombre}:")
        luchar = input("(A)atacar | (C)capturar | (H)huir\n")
        print(miataque)
        print(enemyataque)
        match luchar.lower():

            case "a":
                if random.randint(0,1) == 0:
                    if miataque >= enemydef:
                        enemypsactual = enemypsactual - (miataque - enemydef)
                        print(f"{mipokemon.get_nombre()} ataca.")
                        print(
                            f"{mipokemon.get_nombre()} ha hecho {miataque-enemydef} de daño.")
                        enemydef = 0
                    else:
                        print(f"{mipokemon.get_nombre()} ataca.")
                        print(
                            f"{mipokemon.get_nombre()} ha quitado {miataque} de defensa.")
                        enemydef = enemydef - miataque
                else:
                    print(f"{mipokemon.get_nombre()} ataca y falla.")

                if enemypsactual <= 0:
                    print(f"{pokemonsalvaje.get_nombre()} ha muerto.")
                    return True
                
                print(f"Turno de {pokemonsalvaje.get_nombre()}")
                if random.randint(0,2) == 0:
                    if enemyataque >= midef:
                        mipsactual = mipsactual - (enemyataque - midef)
                        print(f"{pokemonsalvaje.get_nombre()} ataca.")
                        print(
                            f"{pokemonsalvaje.get_nombre()} hace {enemyataque - midef} de daño.\n")
                        midef = 0
                    else:
                        print(f"{pokemonsalvaje.get_nombre()} ataca.")
                        print(
                            f"{pokemonsalvaje.get_nombre()} ha quitado {enemyataque} de defensa.")
                        midef = (midef - enemyataque)
                else:
                    print(f"{pokemonsalvaje.get_nombre()} ataca y falla.")

                if mipsactual <= 0:
                    print(f"Tu pokemon {mipokemon.get_nombre()} a muerto\n")
                    p1.inventario.remove(mipokemon)
                    if len(p1.inventario) == 0:
                        print("No te quedan pokemons para pelear")
                        break
                    else:
                        newpokemon = (p1.inventario[escoger_pokemon()])
                        return newpokemon

            case "c":
                p1.capturar_pokemon(pokemonsalvaje, enemypsactual, enemypsmax)
                return True

            case "h":
                mipokemon.set_ps(mipsactual)
                return True

def sin_pokemon():
    print("Has matado a todos los pokemons.\n")
    seguir = input("¿Quieres jugar de nuevo?")

    match seguir.lower():

        case "s":
            lado=int(input("Indica el tamaño del mapa:\n"))
            mapa_pokemon.Set_lado(lado)
            mapa_pokemon.mapa = []
            mapa_pokemon.generar_mapa()
            mapa_pokemon.pokemon_mapa(almacen[10],2,2)
            mapa_pokemon.añadir_pokemons()

        case "n":
            return False

opciones = {
    "W": "Mover arriba.",
    "D": "Mover derecha.",
    "S": "Mover abajo.",
    "A": "Mover izquierda.",
    "I": "Mirar inventario pokemon.",
    "L": "Para llamar a un pokemon aleatorio."
}
almacen = []

with open(r"Programacion\UD4\Pokemon\pokemons.txt", "r") as lista_pokemons:
    for contenedor_texto in lista_pokemons:
        contenedorS_texto = contenedor_texto.strip()
        pokemon = procesar_linea(contenedor_texto)
        almacen.append(pokemon)

mapa_pokemon = Mapa(5)
mapa_pokemon.generar_mapa()
mapa_pokemon.añadir_pokemons()

p1 = Jugador(1, 1, "alan")

salir = True

while salir:
    if len(mapa_pokemon.hay_pokemon()) == 0:
        sin = sin_pokemon()
        if sin == False:
            break


    mapa_pokemon.mostrar_mapa()
    print("")
    print(f"{p1.nombre}(x:{p1.x},y:{p1.y}) | Total pokemons: {len(p1.inventario)}\n")

    for key, value in opciones.items():
        print(f"Pulsa {key} para: {value}")

    print("")

        
    while True:
        move = input("Que quieres hacer?\n")
        if move == "w" or move == "d" or move == "s" or move == "a" or move == "i" or move == "l":
            break

    match move.lower():

        case "w":
            if p1.y < mapa_pokemon.lado:
                p1.mover_arriba()
        case "d":
            if p1.x < mapa_pokemon.lado:
                p1.mover_derecha()
        case "s":
            if p1.y > 1:
                p1.mover_abajo()
        case "a":
            if p1.x > 1:
                p1.mover_izquierda()
        case "i":
            if len(p1.inventario) == 0:
                print(f"{p1.nombre} no tienes pokemons, llama a un pokemon.")
            else:
                for i in p1.inventario:
                    print(i.mostrar_info())
                print("")
        case "l":
            p1.llamar_pokemon()

    for i in mapa_pokemon.mapa:

        if i[1][0] == p1.x and i[1][1] == p1.y:
            if i[0] != None:
                print(
                    f"Te has encontrado a {i[0].get_nombre()} de tipo {i[0].get_tipo()}")
                i[0].elemento()

                if len(p1.inventario) == 0:
                    print("Como no tienes pokemons, te daremos uno\n")
                    p1.llamar_pokemon()

                while i[0] != None:
                    select_pokemon = (p1.inventario[escoger_pokemon()])
                    print(f"Te escojo a ti {select_pokemon.get_nombre()}")
                    resultado = combate_pokemon(select_pokemon, i[0])

                    match resultado:

                        case True:
                            i[0] = None
                            break
                        case _:
                            combate_pokemon(resultado, i[0])
