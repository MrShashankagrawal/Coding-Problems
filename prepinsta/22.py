def per(n, r):
    pr = n - r
    p = 1
    for i in range(1, n + 1):
        p *= i
    for j in range(1, pr + 1):  # Correct the range for the second loop
        p /= j  # Instead of pr *= j, divide by j to calculate the factorial of (n-r)

    return p

p = int(input("Enter the value of n: "))
r = int(input("Enter the value of r: "))
print(per(p, r))
