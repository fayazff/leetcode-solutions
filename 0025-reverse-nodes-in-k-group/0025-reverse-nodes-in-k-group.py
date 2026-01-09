# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy=ListNode(0)
        dummy.next=head
        prev=dummy
        cur=prev.next
        counter=0
        while cur:
            cur=cur.next
            counter += 1
        while counter>=k:
            cur=prev.next
            nxt=cur.next
            for _ in range(1,k):
                cur.next=nxt.next
                nxt.next=prev.next
                prev.next=nxt
                nxt=cur.next
            prev=cur
            counter-=k
        return dummy.next
        

