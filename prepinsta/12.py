#strong number
n = 145
a = []
for i in str(n):
    f =1
    for j in range(1,int(i)+1):
        f*=j
    a.append(f)
b = sum(a)
if b==n:
    print("ss")
else:
    print("ww")