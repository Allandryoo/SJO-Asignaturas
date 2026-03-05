alumnos = {"alan": 10,
           "ionut": 3,
           "boy": 6,
           "carlos": 4,
           "patricio": 7}
alumnos_aprobados = {}
for key, value in alumnos.items():
    if value >= 5:
        alumnos_aprobados.update({key: value})

print(alumnos_aprobados)
