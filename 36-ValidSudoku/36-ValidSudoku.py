# Last updated: 3/29/2025, 11:53:59 PM
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set) # key :row index , value : set of numbers in it 
        columns = defaultdict(set)
        squares= defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] ==".":
                    continue
                if (board[r][c] in rows[r] ) or board[r][c] in columns[c] or board[r][c] in squares[(r//3,c//3)]:
                    return False 

                rows[r].add(board[r][c])
                columns[c].add(board[r][c])
                squares[(r//3,c//3)].add(board[r][c])

        return True 

        