mat = [[0, 1, 2], [0, 2, 2], [0, 1, 8]]
ls1 = []
ls2 = []

# Loop through the columns and rows
for i in range(len(mat[0])):
    for j in range(len(mat)):
        ls1.append(mat[j][i])

# Create ls2 with diagonal elements of mat in decreasing order
for i in range(len(mat) - 1, -1, -1):
    ls2.append(mat[i][i])

# Extract the unique elements from ls1 to get the desired output
output_ls = sorted(list(set(ls1)), reverse=True)

print(output_ls)
print(ls2)



