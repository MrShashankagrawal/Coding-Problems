n = 33
ls1 = []
ls2 = []

while n > 0:
    s = n // 8
    ls1.append(s)
    b = n % 8
    ls2.append(b)
    n = s

ls2.reverse()

for i in ls2:
    print(i, end="")
