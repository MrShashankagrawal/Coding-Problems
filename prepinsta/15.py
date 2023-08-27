# Example
# Input : 21
# Output : Yes ' It's a Harshad Number.
# Explanation : The sum of the digits of 21 is 3 i.e 2 + 1. As the number 21 is divisible by 3, It's a Harshad N
n = 21
l = str(n)
ls = list(map(int,l))
b= sum(ls)
if n%b==0:
    print("y")
else:
    print("n")