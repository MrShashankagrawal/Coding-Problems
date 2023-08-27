n = int(input())
for i in range (n):
    a = input()
    ls = a.split()
    ls = [int(i) for i in ls]
    if (ls[0]+ls[1])>6:
        print("YES")
    else:
        print("NO")