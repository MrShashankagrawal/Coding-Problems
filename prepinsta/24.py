n = 120909091000
# n = 12191
a = str(n)
ls = list(map(int,a))
print(ls)
ls2=[]
for i in ls:
    if i==0:
        ls2.append(1)
    else:
        ls2.append(i)
for i in ls2:
    print(i,end="")