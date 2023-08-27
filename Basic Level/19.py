# Write a program that will take user input of (4 digits number) and
# check whether the number is narcissist number or not.

n = 1234
a = str(n)
b = list(map(int,a))
c = [i**4 for i in b]
d = sum(c)
print(d)
if 1000<=n<=9999:
    if n ==d:
        print("nars")
    else:
        print("no nars")
else:
    print("no a 4 digi")

