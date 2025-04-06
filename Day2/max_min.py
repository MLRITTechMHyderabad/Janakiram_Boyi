rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
matrix = []
print("Enter the matrix elements row-wise:")

for i in range(rows):
    row = []
    for j in range(cols):
        num = int(input()) 
        row.append(num)
    matrix.append(row)

max_element = matrix[0][0]
min_element = matrix[0][0]

for i in range(rows):
    for j in range(cols):
        if matrix[i][j] > max_element:
            max_element = matrix[i][j]
        if matrix[i][j] < min_element:
            min_element = matrix[i][j]


print("Maximum Element:", max_element)
print("Minimum Element:", min_element)
