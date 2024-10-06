# 206 Reverse Linked List
# 連結リストを反転させる

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# iterative
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
        return prev
    
# stack
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None

        stack = []

        while head.next:
            stack.append(head)
            head = head.next

        while stack:
            cur = stack.pop()
            cur.next.next = cur
            cur.next = None

        return head
    
# 