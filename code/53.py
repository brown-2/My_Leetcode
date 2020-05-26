from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        l = [0] + nums.copy()
        for i in range(1, len(l)):
            l[i] += l[i-1]

        ul = [(0, l[0])]
        for i, o in enumerate(l):
            if o < ul[-1][1]:
                ul.append((i, o))

        dl = [(len(l) - 1, l[-1])]
        for i in range(len(l)):
            ix = len(l) - i - 1
            if l[ix] > dl[-1][1]:
                dl.append((ix, l[ix]))
        for i in ul:
            for j in dl:
                if i[0] >= j[0]:
                    break
                if j[1] - i[1] > res:
                    res = j[1] - i[1]
        print(ul, dl)
        return res



def main():
    obj = Solution()
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    nums = [-2, -1]
    nums = [-1]
    print(obj.maxSubArray(nums))


if __name__ == '__main__':
    main()
