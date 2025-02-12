# Problem: Valid Sudoku - https://leetcode.com/problems/valid-sudoku/

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
    
        for r in range(9):
            row = set()
            col = set()
            for c in range(9):
                # check row
                if board[r][c] != '.' and board[r][c] in row:
                    return False
                row.add(board[r][c]) 
                # check column
                if board[c][r] != '.' and board[c][r] in col:
                    return False
                col.add(board[c][r]) 
                #  check 3 x 3
        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                box = set()
                for i in range(r, r + 3):
                    for j in range(c, c + 3):
                        if board[i][j] != "." and board[i][j] in box:
                            return False
                        else:
                            box.add(board[i][j])                                    
        return True 
            