low,high=8,100000
for k in range(low,high+1):
    a = str(k)
    lent=len(a)#123 =3
    ls = list(map(int,a))
    power = [j**lent for j in ls]
    suma = sum(power)

    if suma==k:
      print(k,end = " ")