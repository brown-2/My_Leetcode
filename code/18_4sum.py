from typing import List
from timeit import default_timer
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort() 
        try:
            for i in range(len(nums)):
                if nums[i] < target - sum(nums[-3:]) or sum(nums[i:i+4]) > target:
                    continue
                try:
                    for j in range(i + 1, len(nums)):
                        sum2 = nums[i] + nums[j]
                        if sum2 < target - sum(nums[-2:]) or sum2 + sum(nums[j+1:j+3]) > target:
                            continue
                        try:
                            for k in range(j + 1, len(nums)):
                                sum3 = sum2 + nums[k]
                                if sum3 < target - nums[-1] or sum3 + nums[k+1] > target:
                                    continue
                                try:
                                    for l in range(k + 1, len(nums)):
                                        if sum3 + nums[l] == target and \
                                                [nums[i], nums[j], nums[k], nums[l]] not in res:
                                            res.append([nums[i], nums[j], nums[k], nums[l]])
                                except IndexError:
                                    pass
                        except IndexError:
                            pass
                except IndexError:
                    pass
        except IndexError:
            pass


        return res

        


def main():
    obj = Solution()
    nums = [-3,-1,0,2,4,5]
    nums = [1, 0, -1, 0, -2, 2]
    nums = [-1,0,1,2,-1,-4]
    nums = [5,5,3,5,1,-5,1,-2]
    nums = [-3,-2,-1,0,0,1,2,3]
    target = 0
    print(obj.fourSum(nums, target))


if __name__ == '__main__':
    main()
