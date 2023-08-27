# Example
# Input : 28
# Divisors : [1, 2, 4, 7, 14]
# Sum = 1 + 2 + 4 + 7 + 14 = 28
# Output : It's a Perfect Number
n = 29
a = []
for i in range(1,n):
    if n%i==0:
        a.append(i)
b = sum(a)
if b==n:
    print("p")
else:
    print("n0")