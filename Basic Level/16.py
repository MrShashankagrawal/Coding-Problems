# Write a program that will determine weather when the value of temperature and humidity is provided by the user.
# TEMPERATURE(C)
# HUMIDITY(%)

t=int(input())
h =int(input())
if t>=30 and h >=90:
    print("h & h")
elif t>=30 and h<90:
    print("h")
elif t<30 and h>=90:
    print("c & h")
else:
    print("c")