# Write a code to reverse a number
n = 1234
st = str(n)
ls = list(map(int,st))
ls.reverse()
for i in (ls):
    print(i,end = "")
