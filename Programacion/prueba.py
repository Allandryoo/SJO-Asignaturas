Diccionario = {}

palabras = ["Arbol", "Astronomía", "Algoritmo", "Abaco", "Alianza",
            "Barco", "Biología", "Brújula", "Binario", "Ballena",
            "Cielo", "Código", "Ciencia", "Computadora", "Cristal",
            "Dado", "Dinosaurio", "Delfín", "Datos", "Diamante",
            "Estrella", "Energía", "Espejo", "Elefante", "Enigma",
            "Fuego", "Física", "Fuente", "Flecha", "Fénix",
            "Galaxia", "Globo", "Gato", "Gravedad", "Guitarra",
            "Hierro", "Horizonte", "Hielo", "Historia", "Hormiga",
            "Isla", "Idea", "Infinito", "Iguana", "Imagen",
            "Jardín", "Juego", "Júpiter", "Joya", "Jirafa"]


for l in palabras:
    primeraletra = l[0].upper()
    if primeraletra not in Diccionario:
        Diccionario[primeraletra] = []

    Diccionario[primeraletra].append(l)

print(Diccionario)
