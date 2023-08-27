# prime factor
n=30
ls = []
for i in range(2,n):
    if n%i==0:
        ls.append(i)
    for j in (ls):
        if j%i==0:
            ls.remove(j)
    for k in (ls):
        print(k,end = " ")
    
    