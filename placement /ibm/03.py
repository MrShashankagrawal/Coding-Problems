# 1 3 2 5 5 ans 4 
ls = [2,3,5,2,4]
a = len(ls)
ls1=[]
for i in range(1,a+1):
    ls1.append(i)
print(ls1)
for i in ls1:
    if i not in ls:
        print(i)