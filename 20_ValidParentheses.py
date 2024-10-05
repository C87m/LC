# 20 Valid Parentheses
# 括弧を含む文字列　括弧が閉じているか？

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dict = {")": "(", "}": "{", "]": "["}
        for char in s:
            if char in dict.values():
                stack.append(char)
            elif char in dict.keys():
                if stack == [] or dict[char] != stack.pop(): # 末尾を取り出す
                    return False
            else:
                return False
        return stack == []
        