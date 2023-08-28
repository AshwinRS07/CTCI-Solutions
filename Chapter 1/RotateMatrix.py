# Implement a method to perform basic string compression using the counts of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the
# "compressed" string would not become smaller than the original string, your method should return the original string. You can assume the string has only uppercase and lowercase letters (a - z).


# Also done on Leetcode: Neetcode's idea
def rotate_matrix(matrix: list[list[int]]) -> list[list[int]]:
    left, right = 0, len(matrix) - 1
    while left < right:
        for i in range(right-left):
            top, bottom = left, right
            topLeft = matrix[top][left+i]
            matrix[top][left+i] = matrix[bottom-i][left]
            matrix[bottom-i][left] = matrix[bottom-i][right-i]
            matrix[bottom-i][right-i] = matrix[top+i][right]
            matrix[top+i][right] = topLeft
        r -= 1
        l += 1
    return matrix