alumnos={"Alan": {"edad" : 23, "nota" : 5}, "Marta": {"edad": 21, "nota": 8}}
suma=0
nota_media=0
for key, value in alumnos.items():
    suma+=value["nota"]
    nota_media=suma/len(alumnos.keys())
print(nota_media)
        