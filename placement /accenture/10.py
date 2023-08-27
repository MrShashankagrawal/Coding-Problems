def rp(n, st, ch1, ch2):
    ls = list(st)
    ls2 = []

    for i in ls:
        if i == ch1:
            ls2.append(ch2)
        elif i == ch2:
            ls2.append(ch1)
        else:
            ls2.append(i)

    result = ''.join(ls2)
    return result

n = int(input("Enter the length of the string: "))
st = input("Enter the string: ")
ch1 = input("Enter character 1: ")
ch2 = input("Enter character 2: ")

output = rp(n, st, ch1, ch2)
print(output)
