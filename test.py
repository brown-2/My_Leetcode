from typing import List
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        record = []
        while '()' in s:
            record.append(s.index('()'))
            s = s.replace('()', '', 1)
        return record




def main():
    obj = Solution()
    s = "(()())((())"
    print(obj.longestValidParentheses(s))


if __name__ == '__main__':
    main()
