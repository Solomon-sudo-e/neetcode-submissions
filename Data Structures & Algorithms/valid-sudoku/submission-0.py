class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        columns = [set() for _ in range(9)]
        boxes = [[set() for _ in range(3)] for _ in range(3)]
        for i in range(len(board)):
            row = set()
            for j in range(len(board)):
                val = board[i][j]
                if val != ".":
                    if val not in boxes[int(i/3)][int(j/3)] and val not in row and val not in columns[j]:
                        boxes[int(i/3)][int(j/3)].add(val)
                        row.add(val)
                        columns[j].add(val)
                    else:
                        return False
        return True
