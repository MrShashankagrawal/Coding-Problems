#prime
n = int(input())
flag = 0 
for i in range(2,n):
    if n%i==0:
        set = 1
    break
if (set==1):
    print(" not prime")
else:
    print("prime")
