from typing import List
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        #breakpoint()
        res = []
        filtered = list(filter(lambda x: x <= target, candidates))
        print(target, filtered)
        if not filtered:
            return None
        if len(filtered) == 1:
            if target == filtered[0]:
                return [[target]]
            else:
                return None
        
        terms = self.combinationSum2(filtered[1 : ], target - filtered[0])
        if terms:
            for term in terms:
                res.append([filtered[0]] + term)
        terms = self.combinationSum2(filtered[1 : ], target)
        if terms:
            for term in terms:
                res.append(term)
        if filtered[0] == target:
            res.append([target])

        for l in res:
            l.sort()
        res.sort()
        for i in range(len(res)):
            try:
                if res[i] == res[i + 1]:
                    res[i] = None
            except IndexError:
                pass
        res = [x for x in res if x]
        return res


                    
                    


def main():
    obj = Solution()
    candidates = [2,5,2,1,2]; target = 5
    print(obj.combinationSum2(candidates, target))
    


if __name__ == '__main__':
    main()

