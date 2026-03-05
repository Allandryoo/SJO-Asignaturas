alumnos = {"alan": {"nota": 10},
           "ionut": {"nota": 3},
           "boy": {"nota": 6},
           "carlos": {"nota": 4},
           "patricio": {"nota": 7}}
alumnos_aprobados = {}
for key, value in alumnos.items():
    if value["nota"] >= 5:
        alumnos_aprobados.update({key: value})

print(alumnos_aprobados)
