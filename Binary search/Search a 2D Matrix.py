class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        u, d = 0, len(matrix) - 1
        while u <= d:
            mR = u + (d-u) // 2
            if matrix[mR][0] > target:
                d = mR - 1
            elif matrix[mR][-1] < target:
                u = mR + 1
            else:
                break
        
            
        l, r = 0, len(matrix[mR]) - 1
        
        while l <= r:
            mC = l + (r - l) // 2
            if matrix[mR][mC] == target:
                return True
            elif matrix[mR][mC] > target:
                r = mC - 1
            else:
                l = mC + 1
        
        return False