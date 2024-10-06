# 283 Move Zeroes
# リストの0を末尾に移動する

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        for i in range(1, len(nums)+1):
            if nums[-i] == 0: # 最初から数えるとうまくいかないので後ろから数える
                nums.pop(-i)
                nums.append(0)