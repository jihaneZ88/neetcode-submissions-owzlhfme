class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:           
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)  # Keyed by (row // 3, col // 3)

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == '.':
                    continue
                    
                # Check if the value is already in the current row, column, or 3x3 square
                if val in rows[r] or val in cols[c] or val in squares[(r // 3, c // 3)]:
                    return False
                    
                # Add the value to the respective sets
                rows[r].add(val)
                cols[c].add(val)
                squares[(r // 3, c // 3)].add(val)

        return True