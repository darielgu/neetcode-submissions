class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n <= 0:
            return [""]
        board = [["."]*n for _ in range(n)]
        columns = set()
        pos_diag = set()
        neg_diag = set()
        res = []
        def backtrack(row):
            
            if row == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
            for column in range(n):
                if column in columns or (row - column) in pos_diag or (row + column) in neg_diag:
                    continue
                columns.add(column)
                pos_diag.add(row-column)
                neg_diag.add(row+column)
                board[row][column] = "Q"
                backtrack(row+1)
                columns.remove(column)
                pos_diag.remove(row-column)
                neg_diag.remove(row+column)
                board[row][column] = "."
        backtrack(0)
        return list(res)