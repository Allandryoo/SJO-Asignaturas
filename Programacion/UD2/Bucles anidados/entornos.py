vip = 15
premium = 10
basica = 5
precio_base = 0
precio_final = 0
descuento = 0

atender = input("Quiere atender un nuevo cliente?\n").lower()

while atender == "si" :
    print("Tipo de entradas: vip 15€, premium 10€, básica 5€")
    entrada = input("Que entrada quiere?\n").lower()
    while entrada != "vip" and entrada != "premium" and entrada != "basica":
        entrada = input("Indique una entrada valida:\n").lower()

    if entrada == "vip":
        precio_base = vip
        print("Has elegido la vip")
    elif entrada == "premium":
        precio_base = premium
        print("Has elegido la premium")
    elif entrada == "basica":
        precio_base = basica
        print("Has elegido la basica")

    edad = int(input("Indique la edad"))

    if edad < 10:
        descuento = 0.35
    elif 10 <= edad <= 18:
        descuento = 0.2
    elif edad >= 65:
        descuento = 0.5
    else:
        descuento=0

    precio_final = precio_base - (precio_base*descuento)

    print(precio_final)

    atender = input("Quiere atender un nuevo cliente?\n").lower()

print("Te has quedado sin helado")

