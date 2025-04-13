# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        res = ListNode(0, head)
        dum = res

        while n != 0:
            head = head.next
            n -= 1

        while head:
            head = head.next
            dum = dum.next
        dum.next = dum.next.next
        return res.next