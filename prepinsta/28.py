dicc = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14}
n = "2A3"  # ans 675

ls = list(n)
ls1 = []
for i in ls:
    if i.isdigit():
        ls1.append(int(i))
    else:
        ls1.append(dicc[i])

res = 0
for i in ls1:
    res = res * 16 + i

print(res)
