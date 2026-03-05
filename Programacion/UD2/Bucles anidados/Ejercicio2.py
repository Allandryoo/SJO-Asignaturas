n=60
numero=[2,5,3]

for i in range(1,n+1):
    for lista in numero:
        if i%lista!=0:
            break
    else:
        print(i)