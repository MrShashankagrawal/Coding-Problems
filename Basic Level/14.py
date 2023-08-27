h = int(input())
m = int(input())
if h<0 and m==0:
    a = h*30
else:
    h = (h+(m/60))*30
    m = m*6
    a = abs(h-m)
print(a)
    