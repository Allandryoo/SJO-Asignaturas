def leer_archivo(ruta):
    lista_alumnos = []
    with open(ruta, "r") as f:
        file = f.read().split()
        for line in file:
            line = line.split(";")
            lista_alumnos.append({
                "nombre": line[0], 
                "edad" :line[1], 
                "nota": float(line[2])
                })
    return lista_alumnos

def obtener_aprobado(lista):
    aprobados = []
    for alumno in lista:
        if alumno["nota"] >= 5:
            aprobados.append(alumno)
    return aprobados

def calcular_estadisticas(lista):
    lista_medias=[]
    mayor = 0
    menor = 10
    suma = 0

    for alumno in lista:
        
        suma += alumno["nota"]

        if alumno["nota"] > mayor:
            mayor = alumno["nota"]

        if alumno["nota"] < menor:
            menor = alumno["nota"]
    media = suma/len(lista)
    lista_medias.append({
        "Media":media,
        "Maxima":mayor,
        "Minima":menor
    })
    return lista_medias

def exportar_alumnos(lista, nombre_archivo):
    with open(nombre_archivo+".txt", "w") as new_file:
        new_file.write("INFORME DE ALUMNOS:\n")
        new_file.write("\n")
        for alumno in lista:
            nombre=alumno["nombre"]
            nota=alumno["nota"]
            new_file.write(f"{nombre} - Nota:{nota}\n")

ruta = "usuarios.csv"

alumnos=leer_archivo(ruta)
print(alumnos)

aprobados=obtener_aprobado(alumnos)
print(aprobados)

medias=calcular_estadisticas(alumnos)
print(medias)

name_file=input("Nombre del archivo: ")
exportar_alumnos(alumnos, name_file)
