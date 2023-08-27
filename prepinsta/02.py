num1,num2=2,100
ls =[]
for i in range(num1,num2+1):
  flag = 0
  for j in range(2,i):
     if i%j==0:
          flag=1
          break
  if flag==0:
    ls.append(i)
for k in (ls):
      print(k)
      
          
          
        
            