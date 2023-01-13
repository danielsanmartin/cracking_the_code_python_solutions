
def rotate_matrix(matrix):
    buffer = []

    n = len(matrix[0])-1
    half = int(len(matrix[0])/2) + len(matrix[0])%2
    row_zeros = [0]*n
    
    for i in range(0, half):
        # from top to down
        for j in range(0, half):
            if matrix[i][j] == 0 or matrix[i][n-j] == 0:
                matrix[i] = row_zeros
                break

        #from bottom to
        for l in range(0, half):
            if matrix[n-i][l] == 0 or matrix[n-i][n-l] == 0:
                matrix[n-i] = row_zeros
                break



    return matrix


matrix = [
        [1, 1, 0, 1, 2],
        [4, 5, 0, 7, 2],
        [4, 8, 9,10, 2],
        [4,11,12, 0, 2],
        [4, 3, 3, 3, 3],
    ]

print('\nINPUT:')
for row in range(0, len(matrix)):
    print(matrix[row])

print('\nMODIFIED:')
new = rotate_matrix(matrix)
for row in range(0, len(new)):
    print(new[row])