# 392 Is Subsequence
# 文字列s,t　sがtの一部ならTrue

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        si = 0
        if len(s) == 0:
            return bool(1)
        for ti in range(len(t)):
            if s[si] == t[ti]:
                si += 1
            if si == len(s):
                return bool(1)
        return bool(0)