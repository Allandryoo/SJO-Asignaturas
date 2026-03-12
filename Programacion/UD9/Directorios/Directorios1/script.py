import os, shutil

lista_archivos = os.listdir(".")

for i in lista_archivos:
    ip = i.split(".")
    if len(ip) > 1:
        if ip[0] != "log" and ip[-1] == "txt":
            if not os.path.exists("textos"):
                os.mkdir("textos")
            shutil.move(i, "textos/")
            if not os.path.exists("log.txt"):
                with open("log.txt", "w") as log:
                    log.write(f"Movido {i} a textos/\n")
            else:
                with open("log.txt", "a") as log:
                    log.write(f"Movido {i} a textos/\n")
            
        if ip[-1] == "jpg":
            if not os.path.exists("imagenes"):
                os.mkdir("imagenes")
            shutil.move(i, "imagenes/")
            if not os.path.exists("log.txt"):
                with open("log.txt", "w") as log:
                    log.write(f"Movido {i} a imagenes/\n")
            else:
                with open("log.txt", "a") as log:
                    log.write(f"Movido {i} a imagenes/\n")

        if ip[-1] == "csv":
            if not os.path.exists("datos"):
                os.mkdir("datos")
            shutil.move(i, "datos/")
            if not os.path.exists("log.txt"):
                with open("log.txt", "w") as log:
                    log.write(f"Movido {i} a datos/\n")
            else:
                with open("log.txt", "a") as log:
                    log.write(f"Movido {i} a datos/\n")

        #if ip[1] == "py":
        #    if not os.path.exists("programas"):
        #        os.mkdir("programas")
        #        shutil.move(i, "programas/")

print("Archivos organizados :)")