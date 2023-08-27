n = int(input())
ls1 = []
for i in range (n):
    ls = list(map(int,input().split()))
    ls1.append(ls)
    
for item in ls1:
    print(item)