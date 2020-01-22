
from typing import List
class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        return list(str(int(''.join([str(i) for i in A])) + K)) if A != [] else [1]
                    


def main():
    obj = Solution()
    A = [1,2,0,0]; K = 34
    print(obj.addToArrayForm(A, K))
    


if __name__ == '__main__':
    main()

