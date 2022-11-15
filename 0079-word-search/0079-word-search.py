# class Solution:
#     def exist(self, board: List[List[str]], word: str) -> bool:
#         R = len(board)
#         C = len(board[0])
#         visited = set()
        
#         def dfs(r, c, ptr):
#             if ptr == len(word):
#                 return True
            
#             if (r < 0 or c < 0 or
#                r >= R or c >= C or
#                (r, c) in visited or board[r][c] != word[ptr]):
#                 return False
            
#             visited.add((r, c))
#             res = (dfs(r + 1, c, ptr + 1) or 
#                 dfs(r, c + 1, ptr + 1) or
#                 dfs(r - 1, c, ptr + 1) or
#                 dfs(r, c - 1, ptr + 1))
#             visited.remove((r, c))
            
#             return res
        
#         for i in range(R):
#             for j in range(C):
#                 if dfs(i, j, 0):
#                     return True
        
#         return False

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        R = len(board)
        C = len(board[0])
        
        count = defaultdict(int, sum(map(Counter, board), Counter()))
        if count[word[0]] > count[word[-1]]:
            word = word[::-1]
        
        def bounds(r, c):
            if ((r < 0) or (c < 0) or
                (r >= R) or (c >= C)):
                return False
            return True
        
        def dfs(r, c, ptr, visited):
            if ptr == len(word):
                return True
            
            if not bounds(r, c) or (r, c) in visited:
                return False
            
            if board[r][c] == word[ptr]:
                ptr += 1
                visited.add((r,c))
                up = dfs(r - 1, c, ptr, visited)
                if up:
                    return True
                down = dfs(r + 1, c, ptr, visited)
                if down:
                    return True
                left = dfs(r, c - 1, ptr, visited)
                if left:
                    return True
                right = dfs(r, c + 1, ptr, visited)
                if right:
                    return True
                visited.remove((r,c))
            
            return False
        
        for i in range(R):
            for j in range(C):
                if dfs(i, j, 0, set()):
                    return True
        
        return False
                
                
            
            