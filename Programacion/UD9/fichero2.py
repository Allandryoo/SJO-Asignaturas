with open ("Programacion/UD9/peliculas.txt", "r") as peliculas:
    linea = peliculas.read()
    newlinea=linea.strip()
    print(newlinea)