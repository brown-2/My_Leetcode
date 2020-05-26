
from typing import List
class Solution:
    def check_lap(self, i, j):
        if not i or not j:
            return False
        if i[0] > j[1] or i[1] < j[0]:
            return False
        return [min(i[0], j[0]), max(i[1], j[1])]
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        pre_length = len(intervals)
        while True:
            for i in [0] * pre_length:
                interval = intervals.pop(0)
                for j, oj in enumerate(intervals):
                    if self.check_lap(interval, oj):
                        intervals[j] = self.check_lap(interval, oj)
                        break
                else:
                    intervals.append(interval)
            cur_length = len(intervals)
            if pre_length == cur_length:
                break
            pre_length = cur_length
        return intervals





def main():
    obj = Solution()
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    intervals = [[1,4], [4,5]]
    intervals = [[1,2]]
    print(obj.merge(intervals))


if __name__ == '__main__':
    main()
