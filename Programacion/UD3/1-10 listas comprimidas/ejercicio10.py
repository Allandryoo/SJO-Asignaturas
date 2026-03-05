import itertools

numero=[lista for lista in range(1,11)]
permutarnum2=[numeros for numeros in itertools.combinations(numero,2)]
permutarnum3=[numeros for numeros in itertools.combinations(numero,3)]
print(permutarnum2)
print(permutarnum3)
