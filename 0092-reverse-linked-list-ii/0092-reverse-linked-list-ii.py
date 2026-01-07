# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head:
            return
        temp=head
        dummy=ListNode(0)
        dummy.next=head
        prev=dummy
        for _ in range(left-1):
            prev=prev.next
        prevsub=None
        cur=prev.next
        for _ in range(right - left + 1):
            nxt=cur.next
            cur.next=prevsub
            prevsub=cur
            cur=nxt
        prev.next.next=cur
        prev.next=prevsub
        return dummy.next
