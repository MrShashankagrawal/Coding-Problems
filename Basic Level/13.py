# Write a program that will tell whether the given number is divisible
# by 3 & 6

n = 126
b = str(n)
b = list(map(int,b))
b = sum(b)
if (n%2==0) and (b%3==0):
    print("yes")
else:
    print("no")
