numero=int(input("Introduce un numero"))

def primo(n):
    for i in range(2,n):
        if n%i == 0:
            return False
        
    print(f"{n} es primo")
    return True
i=2

while i < numero:
    primo(i)
    i+=1