import random
numaleatorio=random.randint(1,10)
intento=10
print(numaleatorio)
numero=None


while numero!=numaleatorio and intento>0:
    print(f"Intentos: {intento}")
    numero=int(input("Introduce un numero "))
    intento-=1
    if numero==numaleatorio:
        print(f"Acertaste: {numero}")
        break
    else:
        print("Te has quedado sin vidas")