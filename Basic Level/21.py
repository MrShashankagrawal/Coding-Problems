#  Write a menu driven program - 1.cm to ft 2.kl to miles 3.usd to inr
# 4.exit
while True:
    print("converter")

    num1 = int(input("value 1: "))

    print("1.cm to fit\n2.km to miles\n3.usd to inr\n4.exit")
    choice = int(input())
    if choice==1:
        print("cm to fit: ",num1*(.032))
    elif choice==2:
        print("km to miles: ",num1*(.62))
    elif choice ==3 :
        print("usd to inr: ",num1*80)
    else:
        break