notas=[4, 7, 5, 9, 3, 6, 8, 2]
def main():
    notas_subidas = subir_un_punto(notas)
    mostrar_originales_subidas(notas, notas_subidas)

    print("Verion con for clasico:")
    for i in range(len(notas_subidas)):
        print(f"Alumno {i+1}:{notas_subidas[i]}")
    print()

    print("Version con [funcion for in]:")
    mostrar_alumno(notas_subidas)

if __name__== "__main__":
    main()