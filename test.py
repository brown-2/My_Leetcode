from typing import List
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        dp = [heights[0]]
        res = dp[0]
        for i in range(1, len(heights)):
            j = i - 1
            if dp[j] > heights[i]:
                res = max(res, max((dp[-i] * i for i in range(1, len(dp) + 1))))
            while j >= 0:
                if dp[j] > heights[i]:
                    dp[j] = heights[i]
                    j -= 1
                else:
                    break
            dp.append(heights[i])
        res = max(res, max((dp[-i] * i for i in range(1, len(dp) + 1))))
        return res

            




def main():
    obj = Solution()
    heights = [2,1,5,6,2,3]
    print(obj.largestRectangleArea(heights))



if __name__ == '__main__':
    main()
