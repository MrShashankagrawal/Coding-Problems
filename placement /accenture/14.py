# A Python3 program to find a peak element

# Driver code.
arr = [10, 20, 15, 2, 23, 90, 67]
n = len(arr)

# first or last element is peak element
if n == 1:
    peak_index = 0
elif arr[0] >= arr[1]:
    peak_index = 0
elif arr[n - 1] >= arr[n - 2]:
    peak_index = n - 1
else:
    # check for every other element
    for i in range(1, n - 1):
        # check if the neighbors are smaller
        if arr[i] >= arr[i - 1] and arr[i] >= arr[i + 1]:
            peak_index = i
            break

print("Index of a peak point is", peak_index)
