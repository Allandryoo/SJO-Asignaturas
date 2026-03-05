n=20
suma=0
for i in range(1,n):
    for j in range(n-1,1,-1):
        if j + i == n:
            suma=i+j
            print(i,j,suma)
    