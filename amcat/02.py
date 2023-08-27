n = int(input())
a = input().split()
ls = [int(i) for i in a]
ls.sort()
a = len(ls)
for i in range(ls[0],n,2):
    print(i,end = " ")
