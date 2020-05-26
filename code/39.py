
from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        #breakpoint()
        res = []
        filtered = list(filter(lambda x: x <= target, candidates))
        if not filtered:
            return None
        if len(filtered) == 1:
            if target % filtered[0] == 0:
                return [[filtered[0]] * (target // filtered[0])]
            else:
                return None
        
        for i in range(target // filtered[0] + 1):
            #print('testing {} {}'.format(i, filtered[0]), 'target = {}'.format(target))
            terms = self.combinationSum(filtered[1 : ], target - filtered[0] * i)
            if terms:
                for term in terms:
                    res.append([filtered[0]] * i + term)
            if target == filtered[0] * i:
                res.append([filtered[0]] * i)

        return res


                    
                    


def main():
    obj = Solution()
    candidates = [2,3,5]
    candidates = [1]
    candidates = [2,3,6,7]
    target = 9
    print(obj.combinationSum(candidates, target))
    


if __name__ == '__main__':
    main()

