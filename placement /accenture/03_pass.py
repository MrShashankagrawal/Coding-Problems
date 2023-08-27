# // You are given a function.
# // int CheckPassword(char str[], int n);
# // The function accepts string str of size n as an argument. Implement the function which returns 1 if given string str is valid password else 0.
# // str is a valid password if it satisfies the below conditions.

# // – At least 4 characters
# // – At least one numeric digit
# // – At Least one Capital Letter
# // – Must not have space or slash (/)
# // – Starting character must not be a number

# // Assumption:
# // Input string will not be empty.

# // Example:

# // Input 1:
# // aA1_67
# // Input 2:
# // a987 abC012

# // Output 1:
# // 1
# // Output 2:
# // 0

def vp(s):
    if len(s)>=4:
        if any(i.isupper() for i in s ):
            if any (i.isdigit() for i in s):
                if "/" not in s and " " not in s :
                    if not s[0].isdigit():
                        return 1 
    return 0 
s = input()
print(vp(s))

