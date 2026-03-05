BBDD = {
    "matrix": {"nombre": "matrix", "duracion": 90, "genero": "ficcion"},
    "star wars": {"nombre": "star wars", "duracion": 140, "genero": "ficcion"},
    "insidious": {"nombre": "insidious", "duracion": 105, "genero": "terror"}
}

nom = input("ads")

BBDD.pop(nom)

print(BBDD)
