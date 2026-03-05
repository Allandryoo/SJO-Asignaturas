import random
salir = False
discografia = {}
nombres = ["ana ", "maria ", "sandra ", "carla ", "sofia "]
verbos = ["limpia ", "friega ", "barre ", "ordena ", "cocina "]
adjetivos = ["fuerte", "rapido", "feo", "lento", "bonito"]

menu_opciones = ["Salir",
                 "Agregar nombre",
                 "Agregar verbo",
                 "Agregar adjetivo",
                 "Listar nombres",
                 "Listar verbos",
                 "Listar adjetivos",
                 "Crea una frase",
                 "Crea una cancion",
                 "Crea un CD",
                 "Mostrar discografia"]


def numero_random(lista_seleccionada):

    numero_aleatorio = random.randint(0, len(lista_seleccionada)-1)
    return numero_aleatorio


def agregar_nombre():

    añadir_nombre = input("Introduce el nombre a añadir.\n")
    nombres.append(añadir_nombre)
    print(nombres)


def agregar_verbo():

    añadir_verbo = input("Introduce el verbo a añadir.\n")
    verbos.append(añadir_verbo)
    print(verbos)


def agregar_adjetivo():

    añadir_adjetivo = input("Introduce el adjetivo a añadir.\n")
    adjetivos.append(añadir_adjetivo)
    print(adjetivos)


def listar_nombres():

    for i in nombres:
        print(i)


def listar_verbos():

    for i in verbos:
        print(i)


def listar_adjetivos():

    for i in adjetivos:
        print(i)


def crear_frase():

    frase_creada = (nombres[numero_random(
        nombres)]) + (verbos[numero_random(verbos)]) + (adjetivos[numero_random(adjetivos)])
    return frase_creada


def crear_cancion():

    cancion_creada = crear_frase()
    return cancion_creada


def crear_cd(nombre_cd, num_canciones):
    cancion_creada = ""
    for numero_cancion in range(1, num_canciones+1):
        estrofas = int(
            input(f"Cuantas estrofas quieres en tu cancion {numero_cancion}: "))
        versos = int(input("Cuantos versos quieres en cada estrofa: "))
        for i in range(1, estrofas):
            print("")
            for j in range(1, versos):
                cancion_creada += crear_cancion()
        discografia[nombre_cd] = {cancion_creada}


while not salir:

    for indice, opcion in enumerate(menu_opciones):
        print(f"Pulsa {indice} para: {opcion}")

    opcion = int(input("Escoge una opcion: "))

    if opcion == 0:

        salir = True

    elif opcion == 1:

        agregar_nombre()

    elif opcion == 2:

        agregar_verbo()

    elif opcion == 3:

        agregar_adjetivo()

    elif opcion == 4:

        listar_nombres()

    elif opcion == 5:

        listar_verbos()

    elif opcion == 6:

        listar_adjetivos()

    elif opcion == 7:

        frase_creada = crear_frase()
        print(frase_creada)

    elif opcion == 8:

        estrofas = int(input("Cuantas estrofas quieres en tu cancion: "))
        versos = int(input("Cuantos versos quieres en cada estrofa: "))
        for i in range(1, estrofas+1):
            print("")
            for j in range(1, versos+1):
                cancion_creada = crear_cancion()
                print(cancion_creada)
        print("")

    elif opcion == 9:

        nombre_cd = input("Indica el nombre del cd\n")
        num_canciones = int(
            input("Indica el numero de canciones para el cd.\n"))
        crear_cd(nombre_cd, num_canciones)

    elif opcion == 10:

        print(discografia)
