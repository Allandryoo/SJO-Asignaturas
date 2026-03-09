import os, shutil
from datetime import datetime

print("Nuevo inicio.")
nom=input("Indique su nombre: ")

ruta = r"Programacion\UD9\Accesos1\accesos.csv"

if not os.path.exists(ruta):
    with open(r"Programacion\UD9\Accesos1\accesos.csv", "w") as file:
        file.write(f"Usuario: {nom}  | Hora inicio: {datetime.now()}\n")
else:
    with open(r"Programacion\UD9\Accesos1\accesos.csv", "a") as file:
            file.write(f"Usuario: {nom}  | Hora inicio: {datetime.now()}\n")

with open(r"Programacion\UD9\Accesos1\accesos.csv", "r") as file:
            leer = file.readlines()


for i in leer:
        print(i)