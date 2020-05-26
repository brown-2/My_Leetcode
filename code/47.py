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
    def permuteUnique(self, nums):
        p = self.permute(nums)
        res = [tuple(x) for x in p]
        res = list(set(res))
        res = [list(x) for x in res]
        return res


def main():
    obj = Solution()
    nums = [1,1,2]
    print(obj.permuteUnique(nums))


if __name__ == '__main__':
    main()

