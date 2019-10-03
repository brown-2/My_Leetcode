from typing import List
class Solution:
    def f(self, d1, d2):
        res = 0
        coef = 1
        while d1 >= d2:
            d1 -= d2
            res += coef
            d2 += d2
            coef += coef
        return res, d1


    def divide(self, dividend: int, divisor: int) -> int:
        flag = dividend * divisor > 0
        dividend = abs(dividend)
        divisor = abs(divisor)
        res = 0
        while dividend >= divisor:
            count, rem = self.f(dividend, divisor)
            res += count
            dividend = rem
        res = res if flag else -res
        if res > 2 ** 31 - 1 or res < - 2 ** 31:
            return 2 ** 31 - 1
        return res



def main():
    obj = Solution()
    print(obj.divide(10, 3))

    print(obj.divide(7, -3))
    print(obj.divide(-2147483648, -1))

if __name__ == '__main__':
    main()
