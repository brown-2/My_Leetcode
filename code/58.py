from typing import List
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            if s[len(s) - i - 1].isspace():
                if res == 0:
                    continue
                else:
                    break
            res += 1
        return res
        


def main():
    obj = Solution()
    s = "Hello World"
    print(obj.lengthOfLastWord(s))


if __name__ == '__main__':
    main()
