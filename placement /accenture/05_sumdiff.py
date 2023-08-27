n = 3
m = 10
ls = []
ls1 = []
for i in range(1, m + 1):
    ls.append(i)
    if i % n == 0:
        ls1.append(i)
res = [i for i in ls if i not in ls1 ]
print(sum(res)-sum(ls1))
