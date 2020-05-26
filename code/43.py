from typing import List
class Solution:
    def f(self, num):
        d = dict(zip(list('0123456789'), range(10)))
        l = []
        for i in num:
            l.append(d[i])
        res = 0
        for i in l:
            res = res * 10 + i
        return res

    def multiply(self, num1: str, num2: str) -> str:
        return str(self.f(num1) * self.f(num2))


def main():
    obj = Solution()
    num1 = "2" 
    num2 = "3"
    print(obj.multiply(num1, num2))

if __name__ == '__main__':
    main()
