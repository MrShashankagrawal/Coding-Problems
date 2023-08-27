#freindly pair
n1,n2=6,28
l1=[]
l2=[]
for i in range(1,n1):
    if n1%i==0:
        l1.append(i)
for j in range(1,n2):
    if n2%j==0:
        l2.append(j)
a=sum(l1)
b=sum(l2)
if (n1/a)==(n2/b):
    print("f")
else:
    print("nf")
