#binary to decimal
n = int(input())
a = str(n)
ls = list(map(int,a))
a1 = len(ls)
ls.reverse()
ls2 = [2**i for i in (a1)]
print(ls2)


    