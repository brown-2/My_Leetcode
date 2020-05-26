from typing import List
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if intervals == []:
            return [newInterval]
        lapped = []
        for i in range(len(intervals)):
            interval = intervals[i]
            if interval[0] > newInterval[1] or interval[1] < newInterval[0]:
                continue
            lapped.append(i)
        if lapped == []:
            for i in range(len(intervals)):
                if newInterval[1] < intervals[i][0]:
                    intervals.insert(i, newInterval)
                    break
            else:
                intervals.append(newInterval)
            return intervals
        newInterval[0] = min(newInterval[0], intervals[lapped[0]][0])
        newInterval[1] = max(newInterval[1], intervals[lapped[-1]][1])
        for i in reversed(lapped):
            intervals.pop(i)
        intervals.insert(lapped[0], newInterval)
        return intervals
def main():
    obj = Solution()
    intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
    newInterval = [4,8]
    intervals = [[1,3],[6,9]]
    newInterval = [4,5]
    print(obj.insert(intervals, newInterval))
if __name__ == '__main__':
    main()
