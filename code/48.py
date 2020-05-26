from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        nrow = len(matrix)
        ncol = len(matrix[0])
        res = []
        for i in range(ncol):
            res.append([matrix[nrow - j - 1][i] for j in range(nrow)])
        for i in range(nrow):
            for j in range(ncol):
                matrix[i][j] = res[i][j]


def main():
    obj = Solution()
    matrix = \
    [
      [1,2,3],
      [4,5,6],
      [7,8,9]
    ]
    print(obj.rotate(matrix))


if __name__ == '__main__':
    main()
