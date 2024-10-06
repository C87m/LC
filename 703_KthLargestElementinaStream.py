# 703 Kth Largest Element in a Stream
# K番目に大きいスコアを見つける

import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.lists = []
        self.num = k
        for i in nums:
            self.add(i)

    def add(self, val: int) -> int:
        heapq.heappush(self.lists, val) # ヒープ
        if len(self.lists) > self.num: # リストの要素がkより多い間は 
            heapq.heappop(self.lists) # ポップして最小値を取り除く
        return self.lists[0] # k番目に大きい値がリストの0番目になる
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)