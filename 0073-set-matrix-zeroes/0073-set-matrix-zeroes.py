class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][j] = "*"
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "*":
                    for p in range(len(matrix)):
                        if matrix[p][j] != "*":
                            matrix[p][j] = 0
                    for p in range(len(matrix[0])):
                        if matrix[i][p] != "*":
                            matrix[i][p] = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "*":
                    matrix[i][j] = 0
        