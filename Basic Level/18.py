# Write a program that will check whether the number is armstrong
# number or not.

n = int(input())
b = str(n)
c = list(map(int,b))
c_cube = [i**3 for i in c ]
c_sum = sum(c_cube)
# if n == c_sum:
#     print("amstrong")
# else:
#     print("not")
print(c_sum)