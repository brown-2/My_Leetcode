class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        above_list = [x for x in nums if x >= target/3]
        below_list = [x for x in nums if x < target/3]
        if above_list == []:
            return sum(below_list[-3:])
        if below_list == []:
            return sum(above_list[:3])
        repeated = set()
        for i in range(len(nums)):
            try:
                if nums[i] == nums[i+1]:
                    repeated.add(nums[i])
            except IndexError:
                break
        above_set = set(above_list)
        below_set = set(below_list)
        min_diff = max(abs(nums[0] * 3 - target), abs(nums[-1] * 3 - target))
        if len(above_list) >= 2:
            for i in range(len(above_list) - 1):
                for j in range(i + 1, len(above_list)):
                    value = target - (above_list[i] + above_list[j])
                    if value in below_set:
                        return target
                    else:
                        for k in range(1, abs(min_diff)):
                            if value + k in below_set or value - k in below_set:
                                min_diff = k if value + k in below_set else -k
                                break
        if len(below_list) >= 2:
            for i in range(len(below_list) - 1):
                for j in range(i + 1, len(below_list)):
                    value = target - (below_list[i] + below_list[j])
                    if value in above_set:
                        return target
                    else:
                        for k in range(1, abs(min_diff)):
                            if value + k in above_set or value - k in above_set:
                                min_diff = k if value + k in above_set else -k
                                break
        return min_diff + target
def main():
    obj = Solution()
    nums = [0, 0, 0]
    target = 1
    print(obj.threeSumClosest(nums, target))


if __name__ == '__main__':
    main()
