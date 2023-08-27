#User will input (3ages).Find the oldest one

a = int(input())
b = int(input())
c = int(input())

if  a > b :
    print(a)
elif a < b:
    print(b)
elif a>c:
    print(a)
elif a<c:
    print(c)
elif b > c :
    print(b)
else:
    print(c)
