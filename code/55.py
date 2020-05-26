
from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        indices = []
        for i, o in enumerate(nums[:-1]):
            if o == 0:
                indices.append(i)
        for i in indices:
            step = 0
            while i - step >= 0:
                if nums[i - step] > step:
                    break
                step += 1
            else:
                return False
        return True



def main():
    obj = Solution()
    nums = [2,3,1,1,4]
    nums = [3,2,1,0,4]
    print(obj.canJump(nums))


if __name__ == '__main__':
    main()
