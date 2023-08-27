length = int(input())

input_list = input().split()
numbers = [int(num) for num in input_list]

start = input()
end = input()

if start and end:
    start = int(start)
    end = int(end)

    for i in numbers:
        if start <= i <= end:
            print(i, end=' ')
else:
    print(-1)
