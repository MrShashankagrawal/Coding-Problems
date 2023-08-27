# Write a program that will give you the sum of 3 digits
n = int(input())
a = n%10
b = int((n%100)/10)
c = int(n/100)
n = a+b+c
print(n)
