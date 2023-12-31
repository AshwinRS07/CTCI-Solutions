# Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0.


# For O(1) SC, use first row and column values to determine if that row or column respectively needs to be set to 0. Have a single extra variable for the 0,0 position overlap condition.
def zero_matrix(matrix: list[list[int]]) -> list[list[int]]:
    firstRow = False
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                if i == 0:
                    firstRow = True
                else:
                    matrix[i][0] = 0
                matrix[0][j] = 0
    for i in range(len(matrix[0])):
        if matrix[i][0] == 0:
            for j in range(len(matrix)):
                matrix[j][i] = 0
    for i in range(len(matrix)):
        if matrix[0][i] == 0:
            for j in range(len(matrix[0])):
                matrix[i][j] = 0
    if firstRow:
        for i in range(len(matrix[0])):
            matrix[0][i] = 0
    return matrix
