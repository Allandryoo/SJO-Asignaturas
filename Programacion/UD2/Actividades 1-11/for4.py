num=int(input("Introduce un numero para hacer el factorial:\n"))
for i in range(num-1,1,-1):
    num*=i
print(num)