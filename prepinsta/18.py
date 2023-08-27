#lcm
n1,n2=12,16
lcm = None
for i in range(max(n1,n2),(n1*n2)+1):
    if i%n1==i%n2:
        lcm = i 
        break
print(lcm)
