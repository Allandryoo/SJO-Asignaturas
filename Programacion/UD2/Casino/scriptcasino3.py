import random

opciones = ["Salir",
            "Tirar dado",
            "Media aritmetica",
            "Estadisticas",
            "Porcentajes"]
opcion = True
base_datos_dados = []



def lanzar_dado():
    numero = (random.randint(1, 6), random.randint(1, 6))
    base_datos_dados.append(numero)
    pintar_dado(numero[0], numero[1])
    print(base_datos_dados)


def pintar_dado(x, y):
    print("###   ###")
    print(f"#{x}#   #{y}#")
    print("###   ###")


def media():
    sumador = sum(sum(tuplas) for tuplas in base_datos_dados)
    print(sumador)
    contador = len(base_datos_dados)
    media = sumador/contador
    print(media)


def estadisticas():
    for i in range(1,7):
        contador=0
        for dado1, dado2 in base_datos_dados:
            if dado1 ==i:
                contador+=1
            if dado2 ==i:
                contador+=1
        print(f"El dado {i} ha aparecido {contador} veces")

def porcentaje():
    for i in range(1, 7):
        porcentaje = (base_datos_dados.count(i)*100/len(base_datos_dados))
        print(f"El porcentaje de {i} es {porcentaje}%")


while opcion == True:
    print("Indica una opcion:")
    for indice, valor in enumerate(opciones):
        print(f"pulsa {indice} para: {valor}")

    opcion = int(input("Escoge una opcion:\n"))

    if opcion == 0:
        opcion == False
        print("Te has salido del programa")

    elif opcion == 1:
        print("Has tirado un dado")
        lanzar_dado()

    elif opcion == 2:
        print("Has echo una aritmetica")
        media()

    elif opcion == 3:
        print("Has solicitdo las estadisticas")
        estadisticas()

    elif opcion == 4:
        print("Has solicitado el porcentaje de los numeros")
        porcentaje()

    else:
        opcion = int(input("Escoge una opcion:\n"))
