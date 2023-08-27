# n = list(map(int,input().split()))
# print(n)
# Input:

# arr: 12 3 14 56 77 13
# num: 13
# diff: 2
# Output:
# 3
# num 

ls = [12,3,14,56,77,13]
num = 13 
diff = 2 
ls1 = []
for i in (ls):
    if abs(num - i)<= diff:
        ls1.append(i)
ls2 = len(ls1)
print(ls1)
print(ls2)
    