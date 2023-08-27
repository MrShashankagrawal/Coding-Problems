n1,n2=12,16
l1=[]
l2=[]
for i in range(1,n1):
    if n1%i==0:
        l1.append(i)
for j in range(1,n2):
    if n2%j==0:
        l2.append(j)
c = None
for i in (l1):
    if i in (l2):
        if c is None or i>c:
            c = i
print(l1)
print(l2)
print(c)
