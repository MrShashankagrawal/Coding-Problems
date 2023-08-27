# Print all the armstrong numbers in the range of 100 to 1000
# for i in range(100,1001):
for i in range(100,1001):
    a = str(i)
    b = list(map(int,a))
    c = [i**3 for i in b]
    d = sum(c)
    if i==d:
        print(i)
    
