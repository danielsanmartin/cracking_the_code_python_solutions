def rotate_matrix(matrix):
    buffer = []
 
    n = len(matrix[0])-1
    
    for j in range(0, n):
        buffer.append(matrix[0][j])
        matrix[0][j] = matrix[j][n]
        matrix[j][n] = matrix[n][n-j]
        matrix[n][n-j] = matrix[n-j][0]
        matrix[n-j][0] = buffer.pop()

    return matrix


matrix = [
        [1, 1, 1, 1, 2],
        [4, 5, 6, 7, 2],
        [4, 8, 9,10, 2],
        [4,11,12,13, 2],
        [4, 3, 3, 3, 3],
    ]

print('\nINPUT:')
for row in range(0, len(matrix)):
    print(matrix[row])

print('\nMODIFIED:')
new = rotate_matrix(matrix)
for row in range(0, len(new)):
    print(new[row])