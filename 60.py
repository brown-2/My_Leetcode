from typing import List
class Solution:
    def frac(self, n):
        if n <= 1:
            return 1
        else:
            return self.frac(n - 1) * n
    def getPermutation(self, n: int, k: int) -> str:
        rest = []
        k = k - 1
        for i in reversed(range(1, n)):
            t = self.frac(i)
            value = k // t
            rest.append(value)
            k = k % t
        l = list(range(1, n + 1))
        res = []
        for i in rest:
            res.append(l.pop(i))
        res.extend(l)
        return ''.join([str(x) for x in res])


def main():
    obj = Solution()
    n, k = 4, 9
    print(obj.getPermutation(n, k))
    for i in range(1, 24):
        print(obj.getPermutation(n, i))


if __name__ == '__main__':
    main()
