import os, shutil

def organizar_archivos(archivo, extension):
    if not os.path.exists(extension):
        os.mkdir(extension)
    shutil.move(archivo, extension)
    if not os.path.exists("log.txt"):
        with open("log.txt", "w") as log:
            log.write(f"Movido {archivo} a {extension}\n")
    else:
        with open("log.txt", "a") as log:
            log.write(f"Movido {archivo} a {extension}\n")


lista_archivos = os.listdir(".")

for i in lista_archivos:
    ip = i.split(".")
    if len(ip) > 1:
        if ip[0] != "log" and ip[-1] == "txt":
            organizar_archivos(i,ip[-1])
         
print("Archivos organizados :)")