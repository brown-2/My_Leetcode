from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            ordered = ''.join(sorted(list(s)))
            d.setdefault(ordered, [])
            d[ordered].append(s)
        return list(d.values())


def main():
    obj = Solution()
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(obj.groupAnagrams(strs))


if __name__ == '__main__':
    main()
