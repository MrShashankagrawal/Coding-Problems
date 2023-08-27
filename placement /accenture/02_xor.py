# – A denotes AND operation
# – B denotes OR operation
# – C denotes XOR Operation
# 1C0C1C1A0B1
# n = 1C0C1C1A0B1
def bn(s):
    a = int(s[0])
    i = 1
    while i<len(s):
        if s[i] == "A":
            a&=int(s[i+1])
        elif s[i] == "B":
            a|=int(s[i+1])
        elif s[i]=="C":
            a^=int(s[i+1])
        i+=2
    return a  
s = input()
print(bn(s))


