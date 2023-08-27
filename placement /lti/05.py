# Input:  arr[] = {1, 3, 2, 5, 4, 7, 10} 

# Output: 1, 2, 3, 4, 5, 10, 7 

# Smallest value is 1(Odd) so output will be Odd-Even pattern.


arr = [1, 3, 2, 5, 4, 7, 10]
arr.sort()
print(arr)
# [1, 2, 3, 4, 5, 7, 10]
a = min(arr)
ls1=[]
ls2=[]
ls3=[]
for i in arr:
    if i%2==0:
        ls1.append(i)
    else:
        ls2.append(i)
print(ls1)
print(ls2)
# if a%2==0:
#     ls3.append(int(i) for i in range ls1 )



    

