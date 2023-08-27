def move_hyphens_to_front(n):
    ls = list(map(str, n))
    ls1 = []
    ls2 = []
    for i in ls:
        if i == "-":
            ls1.append(i)
        else:
            ls2.append(i)
    ls = ls1 + ls2
    result = ""
    for i in ls:
        result += i
    return result

n= "String-Compare"
# output_str = move_hyphens_to_front(input_str)
print(move_hyphens_to_front(n))
