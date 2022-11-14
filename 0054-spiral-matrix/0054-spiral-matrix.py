class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        visited = set()
        R = len(matrix)
        C = len(matrix[0])
        res = []
        i, j = 0, 0
        curr = 0
        
        while len(visited) < R * C:
            if ((i, j) in visited or (i == R) or (j == C) or (i < 0) or (j < 0)):
                if curr == 0:
                    j -= 1
                    i += 1
                elif curr == 1:
                    i -= 1
                    j -= 1
                elif curr == 2:
                    j += 1
                    i -= 1
                elif curr == 3:
                    i += 1
                    j += 1
                
                curr = (curr + 1) % 4
                continue
                
            res.append(matrix[i][j])
            
            visited.add((i, j))
            
            if curr == 0:
                j += 1
            elif curr == 1:
                i += 1
            elif curr == 2:
                j -= 1
            elif curr == 3:
                i  -= 1
        
        return res
                