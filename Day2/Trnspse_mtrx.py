row = int(input('Enter number of row: '))
col = int(input('Enter number of col: '))

matrix = [[int(input(f'column {j+1} -> enter {i+1} element:')) for j in range(col)] for i in range(row)]
transpose = [[0 for i in range(row)] for j in range(col)]

print()   

print('matrix: ')
for i in matrix:
    print(i)
for i in range(row):
    for j in range(col):
        transpose[j][i] = matrix[i][j]

print()   

print('Transpose of matrix: ')
for i in transpose:
    print(i)