from typing import List
class Solution:
    def myPow(self, x: float, n: int) -> float:
        sign = n > 0
        n = - n if not sign else n
        b = bin(n)[2:]
        res = 1
        for i in reversed(b):
            if i == '1':
                res *= x
            x *= x
        res = 1 / res if not sign else res
        return res


def main():
    obj = Solution()
    x = 2.00000
    n = 10
    print(obj.myPow(x, n))


if __name__ == '__main__':
    main()
