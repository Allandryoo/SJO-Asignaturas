nombre = input("Introduce un nombre\n")

while nombre != "alan":
    nombre=input(f"Hola {nombre}")

    if nombre == "alan":
        print(f"Adios {nombre}")