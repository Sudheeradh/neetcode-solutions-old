class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        counter_x = {}
        counter_y = {}
        counter_box = {}
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] != ".":
                    counter_x[int(board[i][j])] = 1 + counter_x.get(int(board[i][j]), 0)
                    if counter_x[int(board[i][j])] > 1:
                        return False
                
                if board[j][i] != ".":
                    counter_y[int(board[j][i])] = 1 + counter_y.get(int(board[j][i]), 0)
                    if counter_y[int(board[j][i])] > 1:
                        return False
                
                if (i % 3 == 0) and (j % 3 == 0):
                    for k in range(3):
                        for l in range(3):
                            if board[i + k][j + l] != ".":
                                counter_box[int(board[i + k][j + l])] = 1 + counter_box.get(int(board[i + k][j + l]), 0)
                                if counter_box[int(board[i + k][j + l])] > 1:
                                    return False
                    counter_box.clear()
                    
                
            counter_x.clear()
            counter_y.clear()
        return True