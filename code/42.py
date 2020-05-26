from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0
        l = height.copy()
        max_index = l.index(max(l))
        tem = height[0]
        for i in range(max_index):
            if l[i] > tem:
                tem = l[i]
            else:
                l[i] = tem
        tem = height[-1]
        for i in range(len(l) - max_index):
            i2 = len(l) - i - 1
            if l[i2] > tem:
                tem = l[i2]
            else:
                l[i2] = tem
        return sum([l[x] - height[x] for x in range(len(height))])

def main():
    obj = Solution()
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    print(obj.trap(height))


if __name__ == '__main__':
    main()
