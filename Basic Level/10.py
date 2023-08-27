# Write a program that will take user input of cost price and selling
# price and determines whether its a loss or a profit

cp = int(input("cp"))
sp = int(input("sp"))
if sp>cp:
    print("profit",sp-cp)
else:
    print("loss",abs(sp-cp))