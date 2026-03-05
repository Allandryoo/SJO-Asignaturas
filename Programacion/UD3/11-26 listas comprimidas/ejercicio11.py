def suma(n):
    sumador=0
    for i in range(n,11):
        sumador=sumador+i
    return sumador

def multi(n):
    multiplicador=1
    for i in range(n,11):
        multiplicador=multiplicador*i
    return multiplicador

def resta(n):
    restador=0
    for i in range(10,n,-1):
        restador=restador-i
    return restador

def divide(n):
    divisor=0
    for i in range(10,n,-1):
        divisor=divisor/i
    return divisor

sumar=[suma(numero) for numero in range(1,11)]
restar=[resta(numero) for numero in range(1,11)]
multiplicar=[multi(numero) for numero in range(1,11)]
dividir=[divide(numero) for numero in range(1,11)]

print(sumar)
print(restar)
print(multiplicar)
print(dividir)
