# n = int(input())
# arr = list(map(int,input().split()))
arr=[1,8,0,2,3,5,6,9,7]
eve=[]
odd = []
# Second largest among even position elements(1 3 5) is 3
# Second smallest among odd position element is 4
for i in range(len(arr)):
    if i%2==0:
        eve.append(arr[i])
    else:
        odd.append(arr[i])
eves=eve.sort()
odds = odd.sort()
print(eve)
print(odd)
print((eve[-2])+(odd[1]))
