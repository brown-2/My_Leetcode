
from typing import List
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        copy = nums.copy()
        copy.sort();copy.reverse()
        if copy == nums:
            nums.reverse()
            return nums
        for i in range(len(nums) - 1):
            index = i + 1
            if nums[-index] > nums[-index - 1]:
                i1 = - index - 1
                value = min([x for x in nums[-index:] if x > nums[i1]])
                i2 = nums.index(value, - index)
                t = nums[i1]
                nums[i1] = nums[i2]
                nums[i2] = t
                remain = nums[-index:]
                remain.sort()
                nums[-index:] = remain

                break
        return nums




def main():
    obj = Solution()
    nums = [1,1,5]
    #nums = [3,2,1]
    #nums = [1,2,3]
    nums = [1,3,2]
    print(obj.nextPermutation(nums))
if __name__ == '__main__':
    main()
