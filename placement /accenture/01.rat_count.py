r = int(input())
unit=int(input())
n = int(input())
ls = list(map(int,input().split()))
totalfood = r*unit
ls1=[]
sum = 0
for i in (ls):
    sum += i
    ls1.append(i)
    if sum>totalfood:
        break

print(len(ls1))




