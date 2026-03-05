lista=[]
with open ("UD9\peliculas.txt", "r") as peliculas:
    for i in peliculas.readlines():
        separar = i.split(",")
        lista.append(separar)

for l in lista:
    titulo=l[0]
    ano=l[1]
    director=l[2]
    genero=l[3]
    duracionmin=l[4]
    puntuacion=l[5]

    print(titulo)
