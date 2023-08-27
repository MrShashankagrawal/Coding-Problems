ls = [1,2,3,4,5,6,7]
even = []
odd = []
for i in ls:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
even = sum(even)
odd = sum(odd)
print(even*odd)