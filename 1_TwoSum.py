# 1 Two Sum
# 合計値がtargetに一致するリスト内の数字の組合せを探しインデックスを返す

from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d_dict = defaultdict(int) # 辞書の初期化

        l = len(nums)

        for i in range(l):
            if target - nums[i] in d_dict:
                return [i, d_dict[target - nums[i]]]
            d_dict[nums[i]] = i #辞書にない場合はキーとインデックスを追加