# sum:9

# size of Arr = 7

# Arr:5 2 4 3 9 7 1

n = [5,2,4,3,9,7,1]
sum = 9
n.sort()
print(n)
if len(n)<2:
    print("-1")
for i in range(len(n)-1):
    if  n[i]+n[i+1]<sum:
            print(n[i]*n[i+1])
            break
else:
        print("0")
        
    