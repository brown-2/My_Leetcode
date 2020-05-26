from typing import List
import numpy as np
class Solution:
    def check(self, a, nrow, ncol):
        if np.any(a[nrow]) or np.any(a[:, ncol]):
            return False
        for i in range(len(a)):
            for x in [nrow + i, nrow - i]:
                for y in [ncol + i, ncol - i]:
                    if x < 0 or x >= len(a) or y < 0 or y >= len(a):
                        continue
                    if a[x,y]:
                        return False
        return True
    def f(self, a):
        if np.all(a.sum(1)):
            b = []
            for i in range(len(a)):
                s = ['.'] * len(a)
                for j in range(len(a)):
                    if a[i,j]:
                        s[j] = 'Q'
                b.append(''.join(s))

            self.res.append(b)
            return
        cur = int(a.sum())
        for i in range(len(a)):
            if self.check(a, cur, i):
                t = a.copy()
                t[cur, i] = 1
                self.f(t)

        

    def solveNQueens(self, n: int) -> List[List[str]]:
        self.res = []
        a = np.zeros((n,n))
        self.f(a)
        return self.res




def main():
    obj = Solution()
    n = 4
    print(obj.solveNQueens(n))


if __name__ == '__main__':
    main()
