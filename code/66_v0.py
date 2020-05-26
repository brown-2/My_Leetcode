
from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return list(str(int(''.join([str(i) for i in digits])) + 1)) if digits != [] else [1]
                    


def main():
    digits = []
    obj = Solution()
    print(obj.plusOne(digits))


if __name__ == '__main__':
    main()
