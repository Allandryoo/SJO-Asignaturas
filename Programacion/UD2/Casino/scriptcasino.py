import random

numero_caras=random.randint(1,20)

print(f"el numero de caras de hoy es: {numero_caras}")

opciones=["Salir", "Tirar dado", "Media aritmetica", "Estadisticas", "Porcentajes"]
opcion=True
base_datos_dados=[]

def lanzar_dado():
    numero=random.randint(1,numero_caras)
    base_datos_dados.append(numero)
    pintar_dado(numero)
    print(base_datos_dados)


def estadisticas(lista):    
    for i in range(1,numero_caras+1):
        print(f"El dado {i} ha aparecido {lista.count(i)} veces")
        
def porcentaje():
    for i in range(1,numero_caras+1):
        porcentaje=(base_datos_dados.count(i)*100/len(base_datos_dados))
        print(f"El porcentaje de {i} es {porcentaje}%")
    
def pintar_dado(n):
    print("###")
    print(f"#{n}#")
    print("###")

def media():
    sumador=sum(base_datos_dados)
    contador=len(base_datos_dados)
    media=sumador/contador
    print(media)

while opcion == True:
    print("Indica una opcion:")
    for indice,valor in enumerate(opciones):
        print(f"pulsa {indice} para: {valor}")
    
    opcion=int(input("Escoge una opcion:\n"))

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
        estadisticas(base_datos_dados)
    elif opcion == 4:
        print("Has solicitado el porcentaje de los numeros")
        porcentaje()
    else:
        opcion=int(input("Escoge una opcion:\n"))
