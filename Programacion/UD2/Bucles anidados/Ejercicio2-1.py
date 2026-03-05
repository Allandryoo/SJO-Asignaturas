n=60
numero=[2,5,3]

for i in range(1,n+1):
    divide=True
    for lista in numero:
        if i%lista!=0:
            divide=False
    
    if divide==True:
        print(i)