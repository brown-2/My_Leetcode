from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            if row.count('.') + len(set(row)) != 10:
                return False

        for i in range(9):
            col = [x[i] for x in board]
            if col.count('.') + len(set(col)) != 10:
                return False
        for i in range(3):
            for j in range(3):
                subcell = [x[j * 3:j * 3 + 3] for x in board[i * 3:i * 3 + 3]]
                flatten = []
                for line in subcell:
                    flatten.extend(line)
                if flatten.count('.') + len(set(flatten)) != 10:
                    return False
        return True

                    


def main():
    obj = Solution()
    board = \
    [
      ["5","3",".",".","7",".",".",".","."],
      ["6",".",".","1","9","5",".",".","."],
      [".","9","8",".",".",".",".","6","."],
      ["8",".",".",".","6",".",".",".","3"],
      ["4",".",".","8",".","3",".",".","1"],
      ["7",".",".",".","2",".",".",".","6"],
      [".","6",".",".",".",".","2","8","."],
      [".",".",".","4","1","9",".",".","5"],
      [".",".",".",".","8",".",".","7","9"]
    ]
    print(obj.isValidSudoku(board))


if __name__ == '__main__':
    main()
