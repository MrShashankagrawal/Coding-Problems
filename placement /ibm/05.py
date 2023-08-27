# binary to decimal
# 1101 = 13

n = "11101"
ls1 = list(map(int,n))
ls1.reverse()
rs = 0
for i in range(len(ls1)):
    rs+=ls1[i]*(2**i)
print(rs)

