from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        res = []
        for i in range(len(nums)):
            l = nums.copy()
            head = l.pop(i)
            rest = self.permute(l)
            res.extend([[head] + x for x in rest])
        return res



def main():
    obj = Solution()
    nums = [1,2,3]
    print(obj.permute(nums))


if __name__ == '__main__':
    main()
