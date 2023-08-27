# Write a program to print whether a given number is prime number or
# not

n = 5 
if n<1:
    for i in range(1,n+1):
        if n%i==0:
            print("no")
        break
    else:
        print("no")
else:
    print("no")
