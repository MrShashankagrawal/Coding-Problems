# 32. User will provide 2 numbers you have to find the HCF of those 2
# numbers
n = int(input())
arr = list(map(int,input().split()))
p=[]
for i in range(arr):
    for j in range(1,i+1):
     if n%i==0:
        p.append(i)
     else:
        i+=1
print(p)





