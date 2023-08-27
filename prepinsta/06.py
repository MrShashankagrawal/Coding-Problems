n = int(input())
a = str(n)
lent=len(a)#123 =3
ls = list(map(int,a))
cs=[]
for i in (ls):
    cs.append(i**lent)
sum = 0
for j in cs:
    sum+=j
if sum==n:
    print("arm")
else:
    print("not arm")
