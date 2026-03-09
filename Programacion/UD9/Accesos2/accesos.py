import os, shutil
class NotaErronea(Exception):
    pass

def ValidaNota(nota):
    if not nota < 0 and nota > 10:
        raise NotaErronea("Nota no valida")
    
def menu():
    opciones = [
        "Añadir nota nueva.",
        "Mostrar notas alumno.",
        "Ver media notas.",
        "Salir."
    ]

    for indice,opcion in enumerate(opciones):
        print(f"{indice} para: {opcion}")

def introducir_nota():
    try:
        nom=input("Indique el nombre del alumno: ")
    except NotaErronea as e:
        print("!Error:",e)
        
    asig=input("Indique la asignatura: ")
    nota=float(input("Indique la nota: "))
    if not os.path.exists(ruta):
        with open(r"Programacion\UD9\Accesos2\notas.csv", "w") as file:
            file.write("Nombre,Asignatura,Nota\n")
            file.write(f"{nom.lower()},{asig.lower()},{nota}\n")
            file.close()
    else:
        with open(r"Programacion\UD9\Accesos2\notas.csv", "a") as file:
            file.write(f"{nom.lower()},{asig.lower()},{nota}\n")
            file.close()

def media_notas():
    
    lista_notas=[]

    with open(r"Programacion\UD9\Accesos2\notas.csv", "r") as file:
        for indice,line in enumerate(file):
            if indice > 0:
                nota = line.split(",")
                lista_notas.append(float(nota[2]))

    suma = 0
    for i in lista_notas:
        suma += i
    media= suma / len(lista_notas)
    print(lista_notas)
    print(f"la media de notas es: {media}")

def notas_alumno(alumno):
    with open(r"Programacion\UD9\Accesos2\notas.csv", "r") as file:
        for indice,line in enumerate(file):
            if indice > 0:
                linea_alumno=line.split(",")
                if linea_alumno[0] == alumno:
                    print(f"{linea_alumno[0]}, {linea_alumno[2]}")

ruta=r"Programacion\UD9\Accesos2\notas.csv"
salir = False

print("Bienvenido")

while not salir:

    menu()
       
    opcion=int(input(""))

    match opcion:
          
        case 0:
            introducir_nota()

        case 2:
            media_notas()

        case 1:
            nom_alumno = input("Indica el nombre del alumno.\n")
            notas_alumno(nom_alumno)

        case 3:
            salir = True