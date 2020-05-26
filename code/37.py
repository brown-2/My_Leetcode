from typing import List
import numpy as np
class Solution:
    def is_same_subcell(self, a, b):
        if a[0] // 3 == b[0] // 3 and a[1] // 3 == b[1] // 3:
            return True
        else:
            return False


    def construct_rest(self, board):
        rest = {}
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    rest[(i,j)] = [str(x) for x in range(1, 10)]
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                value = board[i][j]
                for x, y in rest:
                    #breakpoint()
                    if (x == i or y == j or self.is_same_subcell((i, j), (x, y)))\
                            and value in rest[(x,y)]:
                        rest[(x,y)].remove(value)
        return rest
    def one_candidate_cells(self, rest):
        res = []
        for index in rest:
            if len(rest[index]) == 1:
                res.append(index)
        return res
    def whether_conflict(self, rest):
        ons = self.one_candidate_cells(rest)
        candidates = [rest[x][0] for x in ons]
        if len(set(candidates)) == len(candidates):
            return False
        for i in range(len(ons)):
            for j in range(i + 1, len(ons)):
                if candidates[i] != candidates[j]:
                    continue
                if self.is_same_subcell(ons[i], ons[j]) or ons[i][0] == ons[j][0] or \
                        ons[i][1] == ons[j][1]:
                    return True
        return False
    def solve(self, board):
        while True:
            rest = self.construct_rest(board)
            if not rest:# 填完
                return board
            if self.whether_conflict(rest):
                return False
            ons = self.one_candidate_cells(rest)
            if ons:
                for x,y in ons:
                    board[x][y] = rest[(x,y)][0]
            else:
                break

        x,y = min(rest, key = lambda x: len(rest[x]))
        for candidate in rest[(x,y)]:
            t_board = [x.copy() for x in board]
            t_board[x][y] = candidate
            res = self.solve(t_board)
            if res:
                return res
    def solveSudoku(self, board: List[List[str]]) -> None:
        res = self.solve(board)
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    board[i][j] = res[i][j]


def main():
    obj = Solution()
    board = \
            [[".",".","9","7","4","8",".",".","."],["7",".",".",".",".",".",".",".","."],[".","2",".","1",".","9",".",".","."],[".",".","7",".",".",".","2","4","."],[".","6","4",".","1",".","5","9","."],[".","9","8",".",".",".","3",".","."],[".",".",".","8",".","3",".","2","."],[".",".",".",".",".",".",".",".","6"],[".",".",".","2","7","5","9",".","."]]
    print(obj.solveSudoku(board))

def check(board):
    a = np.array(board)
    for i in range(9):
        row_i = a[i]
        col_i = a[:,i]
        cel_i = a[(i//3) * 3:(i//3 + 1) * 3, (i%3)*3:(i%3 + 1) * 3]
        for j in row_i, col_i, cel_i:
            eles = j[j != '.']
            if len(eles) != len(set(eles)):
                return False
    return True

if __name__ == '__main__':
    main()
