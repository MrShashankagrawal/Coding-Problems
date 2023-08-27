# Write a program that will give you the in hand salary after
# deduction of HRA(10%),DA(5%),PF(3%), and tax(if salary is between
# 5-10 lakh–10%),(11-20lakh–20%),(20< _ – 30%)(0-1lakh print k).
n = 1000000
hra = .10*n
da= .05*n
pf = .03*n
tt=.10*n + .05*n + .03*n
five_10 = .10*n
elev_20 = .20*n
above_20 = .30*n
if 0<=n<=199999:
    print(n)
elif 200000<=n<=499999:
    print(n-tt)
elif 500000 <=n <=1099999:
    print(n-tt-five_10)
elif 1100000<=n<=2000000:
    print(n-tt-elev_20)
else:
    print(n-tt-above_20)



