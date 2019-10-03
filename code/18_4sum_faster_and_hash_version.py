from typing import List
from timeit import default_timer
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4:
            return []
        res = []
        nums.sort()
        above_list = [x for x in nums if x >= target/4]
        below_list = [x for x in nums if x < target/4]
        if len(above_list) == 0:
            return []
        if len(below_list) == 0:
            if len(above_list) >= 4 and above_list[3] == target/4:
                return [[int(target/4)] * 4]
            else:
                return []
        above_sum2, above_sum3, below_sum2, below_sum3 = {}, {}, {}, {}

        if len(above_list) >= 2:
            right2, left2 = sum(above_list[-2:]), sum(above_list[:2])
            for i in range(len(below_list) - 1):
                if below_list[i] + below_list[-1] + right2 < target\
                        or sum(below_list[i:i+2]) + left2 > target:
                    continue
                for j in range(i + 1, len(below_list)):
                    sum2 = below_list[i] + below_list[j]
                    below_sum2.setdefault(sum2, set())
                    below_sum2[sum2].add((below_list[i], below_list[j]))
        if len(below_list) >= 2:
            right2, left2 = sum(below_list[-2:]), sum(below_list[:2])
            for i in range(len(above_list) - 1):
                if above_list[i] + above_list[-1] + right2 < target or sum(above_list[i:i+2]) + left2 > target:
                    continue
                for j in range(i + 1, len(above_list)):
                    sum2 = above_list[i] + above_list[j]
                    above_sum2.setdefault(sum2, set())
                    above_sum2[sum2].add((above_list[i], above_list[j]))


        if len(below_list) >= 3:
            right2, left2 = sum(below_list[-2:]), sum(below_list[:2])
            for i in range(len(below_list) - 2):
                if below_list[i] + right2 + above_list[-1] < target\
                        or sum(below_list[i:i+3]) + above_list[0] > target:
                    continue
                for j in range(i + 1, len(below_list) - 1):
                    sum2 = below_list[i] + below_list[j]
                    if sum2 + below_list[-1] + above_list[-1] < target\
                            or sum2 + below_list[j + 1] + above_list[0] > target:
                        continue
                    for k in range(j + 1, len(below_list)):
                        sum3 = sum2 + below_list[k]
                        below_sum3.setdefault(sum3, set())
                        below_sum3[sum3].add((below_list[i], below_list[j], below_list[k]))
        if len(above_list) >= 3:
            right2, left_2 = sum(above_list[-2:]), sum(above_list[:2])
            for i in range(len(above_list) - 2):
                if above_list[i] + right2 + below_list[-1] < target\
                        or sum(above_list[i:i+3]) + below_list[0] > target:
                    continue
                for j in range(i + 1, len(above_list) - 1):
                    sum2 = above_list[i] + above_list[j]
                    if sum2 + below_list[-1] + above_list[-1] < target\
                            or sum2 + above_list[j + 1] + below_list[0] > target:
                        continue
                    for k in range(j + 1, len(above_list)):
                        sum3 = sum2 + above_list[k]
                        above_sum3.setdefault(sum3, set())
                        above_sum3[sum3].add((above_list[i], above_list[j], above_list[k]))
        if len(below_sum2) < len(above_sum2):
            d1 = below_sum2
            d2 = above_sum2
        else:
            d1 = above_sum2
            d2 = below_sum2
        for sum2 in d1:
            if target - sum2 in d2:
                for i in d1[sum2]:
                    for j in d2[target - sum2]:
                        res.append(list(i) + list(j))
        below_set = set(below_list)
        above_set = set(above_list)
        for sum3 in below_sum3:
            if target - sum3 in above_set:
                for i in below_sum3[sum3]:
                    res.append(list(i) + [target - sum3])
        for sum3 in above_sum3:
            if target - sum3 in below_set:
                for i in above_sum3[sum3]:
                    res.append(list(i) + [target - sum3])

        if len(above_list) >= 4 and above_list[3] == target/4:
            res.append([int(target/4)] * 4)
        return res


        


def main():
    obj = Solution()
    nums = [-3,-1,0,2,4,5]
    nums = [1, 0, -1, 0, -2, 2]
    nums = [-1,0,1,2,-1,-4]
    nums = [5,5,3,5,1,-5,1,-2]
    nums = [0,0,0, 0]
    nums = [1,4,-3,0,0,0,5,0]
    target = 0
    print(obj.fourSum(nums, target))


if __name__ == '__main__':
    main()
