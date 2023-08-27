input_string = "ssdhjje"
print("Original string:", input_string)

unique_chars = []

for char in input_string:
    if char not in unique_chars:
        unique_chars.append(char)
    else:
        if char in unique_chars:
            unique_chars.remove(char)

print("Unique characters that occur only once:", ''.join(unique_chars))
