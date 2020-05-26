
from typing import List
class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        number = self.countAndSay(n - 1)
        res = []
        last = number[0]
        temp = last
        for i in number[1:]:
            if i == last:
                temp += i
            else:
                res.append(temp)
                temp = i
            last = i
        if temp != '':
            res.append(temp)
        for i in range(len(res)):
            res[i] = '{0}{1}'.format(len(res[i]), res[i][0])
        return ''.join(res)
            






                    


def main():
    obj = Solution()
    print(obj.countAndSay(1))


if __name__ == '__main__':
    main()
