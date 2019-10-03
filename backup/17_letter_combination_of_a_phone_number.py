from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == '':
            return []
        mapping = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl',
                '6':'mno', '7':'pqrs','8':'tuv', '9':'wxyz'}
        if len(digits) == 1:
            return mapping[digits]
        else:
            res = []
            for i in mapping[digits[0]]:
                for j in self.letterCombinations(digits[1:]):
                    res.append(i + j)
            return res
        


def main():
    digits = '23'
    obj = Solution()
    print(obj.letterCombinations(digits))


if __name__ == '__main__':
    main()
