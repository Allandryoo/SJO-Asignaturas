num=int(input("Introduce un numero:\n"))

while num != 0:
    for i in range(1,num):
        if num%i==0:
            print(i)
            
    num=int(input("Introduzca de nuevo un numero:\n"))