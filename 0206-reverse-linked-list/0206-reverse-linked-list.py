# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        prev = None
        cur = head
        nex = cur.next

        while nex != None:
            cur.next = prev
            prev = cur
            cur = nex
            nex = cur.next
        cur.next = prev
        return cur