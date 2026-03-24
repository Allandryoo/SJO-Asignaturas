import os
def leer_texto(ruta):
    with open(ruta, "r") as file:
        lineas = file.readlines()
        for linea in lineas:
            lineaseparada = linea.lower().strip().replace(".", " ").replace(",", " ").split()
            return lineaseparada




def calcular_frecuencia(lista):
    frecuencias = {}
    for palabra in lista:
        if palabra in frecuencias:
            frecuencias[palabra] += 1
        else:
            frecuencias[palabra] = 1
    return frecuencias


    
def generar_ranking(frecuencias):
    lista = list(frecuencias.items())
    ranking = []
    while len(lista) > 0:
        mayor = lista[0]
        for elemento in lista:
            if elemento[1] > mayor[1]:
                mayor = elemento

        ranking.append(mayor)
        lista.remove(mayor)

    return ranking

def exportar_ranking(lista):
    with open("ranking.csv", "w") as registro:
        registro.write("palabra,frequencia\n")
        for pos in lista:
            registro.write(str(f"{pos}\n"))

lista = leer_texto("fichero.txt")

diccionario_frecuencias = calcular_frecuencia(lista)

listaRanking = generar_ranking(diccionario_frecuencias)

exportar_ranking(listaRanking)