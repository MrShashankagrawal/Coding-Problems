# Example

# Input:
# 7
# 12
# Output:
# 8

a1, a2 = 14, 36
max_power_of_2 = -1

for i in range(a2, a1 - 1, -1):
    if (i & (i - 1)) == 0:
        max_power_of_2 = i
        break

print(max_power_of_2)

