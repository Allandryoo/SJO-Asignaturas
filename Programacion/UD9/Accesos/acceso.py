import os
import shutil
from datetime import datetime

nom=input("Nombre de usuario: ")

with open("Programacion/UD9/Accesos/", "a") as file:
    file.write(f"Usuario: {nom}  | Hora inicio: {datetime.now()}")