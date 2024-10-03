# 387 First Unique Character in a String
# 文字列sの中で複数回出現しないアルファベットで一番左にあるもののインデックスを出力なければ-1

from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = Counter(s) #重複をカウントして辞書で返す
        for i in range(len(s)):
            if count[s[i]] == 1:
                return i 
        return -1