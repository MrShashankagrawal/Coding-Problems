length = int(input())

input_list = input().split()
numbers = [int(num) for num in input_list]


numbers.sort()

for i in range(0, length, 2):
    print(numbers[i], end=' ')
print()
