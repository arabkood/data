def rotateMatrix(matrix):
    n = len(matrix)
    transposed = [[matrix[j][i] for j in range(n)] for i in range(n)]
    rotated = [row[::-1] for row in transposed]
    return rotated
