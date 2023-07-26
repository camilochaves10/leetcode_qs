'''Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need 
to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 
without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily 
solvable.
Only the filled cells need to be validated according to the mentioned 
rules.'''

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def col_check(board):
            for i in range(9):
                numbers = {}
                for row in board:
                        if row[i] != '.':
                            if row[i] not in numbers:
                                numbers[row[i]] = 1
                            else:
                                return False
            return True

        def row_check(board):
            for row in board:
                numbers = {}
                #print(row)
                for num in row:
                    if num != '.':
                        if num not in numbers:
                            numbers[num] = 1
                        else:
                            return False
                
            return True
        def square_check(board):
            for i in range(0,9,3):
                numbers = {}
                for row in board[i:i+3]:
                    for num in row[0:3]:
                        if num != '.':
                            if num not in numbers:
                                numbers[num] = 1
                            else:
                                return False
                numbers = {}
                for row in board[i:i+3]:
                    for num in row[3:6]:
                        if num != '.':
                            if num not in numbers:
                                numbers[num] = 1
                            else:
                                return False
                numbers = {}
                for row in board[i:i+3]:
                    for num in row[6:9]:
                        if num != '.':
                            if num not in numbers:
                                numbers[num] = 1
                            else:
                                return False
            return True


        #print(col_check(board))
        print(row_check(board))
        return col_check(board) and row_check(board) and 
square_check(board)
