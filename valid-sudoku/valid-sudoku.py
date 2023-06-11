class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # cache = dict()
        # for i in range(1,10):
        #     cache[str(i)] = set()
        cache = set()
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == '.':
                    continue
                # cell = i//3,j//3
                # row = i + 1,-1
                # col = -1,j + 1
                cell = i//3,j//3,board[i][j]
                row = i,board[i][j]
                col = board[i][j],j
                
                # if cell in cache[board[i][j]]:
                #     return False
                # elif row in cache[board[i][j]]:
                #     return False
                # elif col in cache[board[i][j]]:
                #     return False
                # cache[board[i][j]].add(cell)
                # cache[board[i][j]].add(row)
                # cache[board[i][j]].add(col)
                if cell in cache:
                    return False
                if row in cache:
                    return False
                if col in cache:
                    return False

                cache.add(cell)
                cache.add(row)
                cache.add(col)
        return True