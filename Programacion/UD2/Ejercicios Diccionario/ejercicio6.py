alumno={"nombre": "alan", "edad":23, "curso":"segundo"}

alumno.update({"nota_final":9,"edad":21})

if "nota_final" in alumno:
    print("Existe")
    print(alumno)
else:
    print("No existe")