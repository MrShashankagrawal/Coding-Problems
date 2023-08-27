# Write a program that will take three digits from the user and add
# the square of each digit

n = int(input())
if 100 <=n<=999:
    a1=n%10
    a2=(n%100)//10
    a3=n//100
    print((a1**2)+(a2**2)+(a3**2))
