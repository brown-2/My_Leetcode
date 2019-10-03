from tqdm import tqdm
class Solution:
    def threeSum(self, nums):
        res = []

        nums.sort()
        positive_list = set()
        negative_list = set()
        zero_num = nums.count(0)
        nums = [x for x in nums if x != 0]
        if len(nums) < 3 and zero_num ==0:
            return res

        repeated = set()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                repeated.add(nums[i])
            if nums[i] > 0:
                positive_list.add(nums[i])
            else:
                negative_list.add(nums[i])
        try:
            if nums[-1] > 0:
                positive_list.add(nums[-1])
            else:
                negative_list.add(nums[-1])
        except IndexError:
            pass

        dumpicate = set()
        for i in positive_list:
            for j in positive_list:
                if -(i + j) in negative_list and i != j and (j, i) not in dumpicate:
                    res.append([i, j, -(i + j)])
                    dumpicate.add((i, j))
        for i in negative_list:
            for j in negative_list:
                if -(i + j) in positive_list and i != j and (j, i) not in dumpicate:
                    res.append([i, j, -(i + j)])
                    dumpicate.add((i, j))
        print(res)
        for i in repeated:
            if - i * 2 in negative_list or - i * 2 in positive_list:
                res.append([i, i, - i * 2])

        if zero_num >= 3:
            res.append([0, 0, 0])

        if zero_num >= 1:
            for i in positive_list:
                if -i in negative_list:
                    res.append([0, i, -i])
        
        return res

def main():
    obj = Solution()
    nums = [-1, 0, 1, 2, -1, -4]
    #nums = [0, 0, 0]
    #nums = [3,0,-2,-1,1,2]
    nums = [-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0]
    print(obj.threeSum(nums))


if __name__ == '__main__':
    main()
