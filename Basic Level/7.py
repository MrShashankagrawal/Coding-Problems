# Writeaprogramthatwilltellwhetherthegivenyearisaleapyear
# or not.
n = int(input())
for i in range(n):
# n = (int(n%10),int()
n=((n%100)//10)*10 + n%10
if n%4==0:
    print(n,"It is a leap year")

