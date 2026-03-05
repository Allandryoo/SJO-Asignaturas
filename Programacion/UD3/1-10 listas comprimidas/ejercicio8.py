
def primo(n):
    for i in range(2,n):
        if n%i == 0:
            return False
        
    print(n)
    return True

primos=[primo(primos) for primos in range(1,101)]