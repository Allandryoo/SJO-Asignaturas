def leer_texto(ruta):
    with open(ruta, "r") as file:
        lineas = file.readlines()
        for linea in lineas:
            lineaseparada = linea.lower().strip().replace(".", " ").replace(",", " ").split()
            print(lineaseparada)
            return lineaseparada


lista = leer_texto("fichero.txt")

def calcular_frecuencia(lista):
    frecuencias = {}
    for palabra in lista:
        if palabra in frecuencias:
            frecuencias[palabra] += 1
        else:
            frecuencias[palabra] = 1
    print(frecuencias)
    return frecuencias

diccionario_frecuencias = calcular_frecuencia(lista)
    
def generar_ranking(frecuencias):
    tuplas = frecuencias.items()
    for i in tuplas.sorted(key[1], reverse=True):
        print(i)


generar_ranking(diccionario_frecuencias)