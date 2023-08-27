n = int(input())
ls = [0,1]
if n==0:
    ls=[]
elif n ==1:
    ls=[0]
elif n ==2:
    ls = [0,1]
else:
    for i in range(2,n):
     next = ls[i-1]+ls[i-2]
     ls.append(next)
for j in (ls):
     print(j,end=" ")