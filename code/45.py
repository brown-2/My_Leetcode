from typing import List
class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        length = len(nums)
        res = 0
        index = 0
        while True:
            # breakpoint()
            if nums[index] + index >= length - 1:
                break
            l = nums[index + 1:nums[index] + index + 1]
            l1 = [l[x] + x for x in range(len(l))]
            best = max(range(len(l)), key = lambda x: l1[x])
            index += best + 1
            res += 1
            # print(index)
        return res + 1



def main():
    obj = Solution()
    nums = [2,3,1,1,4]
    nums = [5,6,4,4,6,9,4,4,7,4,4,8,2,6,8,1,5,9,6,5,2,7,9,7,9,6,9,4,1,6,8,8,4,4,2,0,3,8,5]
    print(obj.jump(nums))


if __name__ == '__main__':
    main()
