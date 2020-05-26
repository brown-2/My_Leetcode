from typing import List
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = list(filter(lambda x: x > 0, nums))
        l = [0] * (len(nums) + 1)
        for i in nums:
            try:
                l[i - 1] = 1
            except IndexError:
                continue
        for i in range(len(l)):
            if l[i] == 0:
                return i + 1


def main():
    obj = Solution()
    nums = [7,8,9,11,12]
    nums = [3,4,-1,1]
    nums = [1,2,0]
    print(obj.firstMissingPositive(nums))


if __name__ == '__main__':
    main()
