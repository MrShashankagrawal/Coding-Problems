# # Write a program to find the sum of first n numbers, where n will be
# # provided by the user. Eg if the user provides n=10 the output should be 55.

n = 10 
r = []
# while n<0:
for i in range (1,n+1):
 r.append(i)
 d=sum(r)
print(d) 


# # Input from the user
# n = int(input("Enter a positive integer: "))

# # Initializing variables
# sum_of_numbers = 0
# current_number = 1

# # Calculating the sum of first n numbers
# while current_number <= n:
#     sum_of_numbers += current_number
#     current_number += 1

# # Displaying the result
# print("The sum of the first", n, "numbers is:", sum_of_numbers)
n = 10
s = 0 
c=1
while c<=n:
    s+=c
    c+=1
print(s)
