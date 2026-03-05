import itertools

numero=(1,2,3)
palabra=("CIA")

permutarnum=[numeros for numeros in itertools.permutations(numero)]
permutarpal=[palabras for palabras in itertools.permutations(palabra)]

print(permutarnum)
print(permutarpal)