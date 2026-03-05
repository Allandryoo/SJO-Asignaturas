alumno={"nombre": "alan", "edad":23, "curso":"segundo"}

alumno.update({"nota_final":9,"edad":21})

for key, valor in alumno.items():
    print(key, valor)