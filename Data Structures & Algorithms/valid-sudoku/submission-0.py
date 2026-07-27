class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = []
        columns = []
        squares = {}
        for i in range(9):
            rows.append(set())
            columns.append(set())

        for r in range(9):              # for rows
            for c in range(9):          # for columns
                number = board[r][c]
                if number != '.':
                    box = (r // 3, c // 3)
                    if box not in squares:
                        squares[box] = set()
                    if (number not in rows[r]) and (number not in columns[c]):
                        if number not in squares[box]:
                            rows[r].add(number)
                            columns[c].add(number)
                            squares[box].add(number)
                        else:
                            return False
                    else:
                        return False
        return True
                    
        