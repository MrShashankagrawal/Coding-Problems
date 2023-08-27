# def prime(n):
#     ls = []
#     for i in range(2,n):
#         flag = 0
#         for j in range(2,i):
#             if i%j==0:
#                 flag = 1
#         if flag==0:
#             ls.append(i)
# n = 30
# print(prime(n))

n = 56   
ls = []
for i in range(2,n):
        flag = 0
        for j in range(2,i):
            if i%j==0:
                flag = 1
        if flag==0:
            ls.append(i)
print(ls)

flag = 0
for i in range(len(ls)):
     for j in range(i+1,len(ls)):
            if ls[i]+ls[j]==n:
                flag = 1
                print(ls[i],"+",ls[j],"=",n)
                break
if flag ==0:
     print("no")
     
     
     