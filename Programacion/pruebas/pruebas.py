class Persona:
    def __init__(self, nombre):
        self.nombre = nombre


p1=Persona("Hola1")
p2=Persona("Hola2")
p3=Persona("Hola3")
p4=Persona("Hola4")
p5=Persona("Hola5")
lista1=[p1,p2,p4]
lista2=[p3,p5]

lista2.append(lista1[2])
lista1.pop(2)

for i in lista1:
    print("1")
    print(i.nombre)
for j in lista2:
    print(2)
    print(j.nombre)