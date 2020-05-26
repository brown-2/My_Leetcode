from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if matrix == []:
            reutrn []
        m, n = len(matrix), len(matrix[0])
        res = []
        if m == 1:
            res.extend(matrix.pop(0))
            return res
        if m == 2:
            res.extend(matrix.pop(0))
            res.extend(reversed(matrix[0]))
            return res
        if n == 1:
            res = [x[0] for x in matrix]
            return res
        if n == 2:
            res.extend(matrix.pop(0))
            for i in matrix:
                res.append(i.pop(-1))
            res.extend(reversed([x[0] for x in matrix]))
            return res

        res.extend(matrix.pop(0))
        head, tail = [], []
        for i in matrix:
            head.append(i.pop(0))
            tail.append(i.pop(-1))
        res.extend(tail)
        res.extend(reversed(matrix.pop(-1)))
        res.extend(reversed(head))
        res.extend(self.spiralOrder(matrix))
        return res









def main():
    obj = Solution()
    matrix =  [ [ 1, 2, 3 ], [ 4, 5, 6 ], [ 7, 8, 9 ] ]
    matrix = [
              [1, 2, 3, 4],
                [5, 6, 7, 8],
                  [9,10,11,12]
                  ]

    print(obj.spiralOrder(matrix))


if __name__ == '__main__':
    main()
