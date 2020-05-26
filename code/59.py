from typing import List
class Solution:
    def next(self):
        if self.direction == 'r':
            if self.j == self.n - 1 or self.res[self.i][self.j + 1]!= 0:
                self.direction = 'd'
                self.i += 1
            else:
                self.j += 1
        elif self.direction == 'd':
            if self.i == self.n - 1 or self.res[self.i + 1][self.j]!= 0:
                self.direction = 'l'
                self.j -= 1
            else:
                self.i += 1
        elif self.direction == 'l':
            if self.j == 0 or self.res[self.i][self.j - 1]!= 0:
                self.direction = 'u'
                self.i -= 1
            else:
                self.j -= 1
        elif self.direction == 'u':
            if self.i == 0 or self.res[self.i - 1][self.j]!= 0:
                self.direction = 'r'
                self.j += 1
            else:
                self.i -= 1
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n == 0:
            return [[]]
        self.n = n
        self.res = [[0 for i in range(n)] for i in range(n)]
        self.i, self.j = 0, 0
        self.value = 1
        self.res[self.i][self.j] = self.value
        self.direction = 'r'
        while self.value < n ** 2:
            self.next()
            self.value += 1
            self.res[self.i][self.j] = self.value
        return self.res

def main():
    obj = Solution()
    n = 0
    print(obj.generateMatrix(n))


if __name__ == '__main__':
    main()
