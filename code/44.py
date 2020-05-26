from typing import List
import numpy as np
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if len(p) - p.count('*') > len(s):
            return False
        s = ' ' + s
        p = ' ' + p
        a = np.zeros((len(s), len(p)))
        a[0,0] = 1
        for iP in range(len(p)):
            for iS in range(len(s)):
                if iP == 0 and iS == 0:
                    continue
                if p[iP] == '*':
                    if iS > 0 and (a[iS - 1, iP - 1] or a[iS - 1, iP]) or\
                            (iP > 0 and a[iS, iP - 1]):
                        a[iS, iP] = 1
                elif p[iP] == '?' or p[iP] == s[iS]:
                    if a[iS - 1, iP - 1] and iS > 0 and iP > 0:
                        a[iS, iP] = 1
        return a


def main():
    obj = Solution()
    s = "acdcb"
    p = "a*c?b"

    s = "adceb"
    p = "*a*b"

    s = "mississippi"
    p = "m??*ss*?i*pi"

    print(obj.isMatch(s, p))


if __name__ == '__main__':
    main()
