from typing import List
class Solution:
    def __init__(self):
        self.res = []
    def f(self, s):
        nl = s.count('(')
        nr = s.count(')')
        if nl == self.n:
            s += ')' * (self.n - s.count(')'))
            self.res.append(s)
            return
        elif nr < nl:
            self.f(s + ')')
        self.f(s + '(')
    def generateParenthesis(self, n: int) -> List[str]:
        self.n = n
        self.f('')
        return self.res

        


def main():
    obj = Solution()
    n = 3
    print(obj.generateParenthesis(n))


if __name__ == '__main__':
    main()
