from typing import List
class Solution:
    def isValid(self, s: str) -> bool:
        l = []
        d = {']':'[', '}':'{', ')':'('}
        for i in s:
            if i in '([{':
                l.append(i)
            else:
                try:
                    if d[i] == l.pop(-1):
                        continue
                    else:
                        return False
                except IndexError:
                    return False
        if l == []:
            return True
        else:
            return False

        


def main():
    obj = Solution()
    s = '()'
    #s = '()[]{}'
    #s = '(]'
    #s = '([)]'
    #s = '{[]}'
    print(obj.isValid(s))


if __name__ == '__main__':
    main()
