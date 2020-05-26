
from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits == []:
            return [1]
        digits[-1] += 1
        for i in range(len(digits)):
            index = len(digits) - 1 - i
            if digits[index] == 10:
                digits[index] = 0
                if index == 0:
                    digits.insert(0, 1)
                else:
                    digits[index - 1] += 1
            else:
                break
        return digits

                    


def main():
    obj = Solution()
    for digits in [[], [1,2,3], [9,9]]:
        print(obj.plusOne(digits))


if __name__ == '__main__':
    main()
