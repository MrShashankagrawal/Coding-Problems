n = int(input())
a = input().split()
ls = [int(i) for i in a]
start = int(input())
end = int(input())
rs = False
for i in (ls):
    if start<=i<=end:
        print(i,end=" ")
        rs = True

if not rs:
    print(-1)