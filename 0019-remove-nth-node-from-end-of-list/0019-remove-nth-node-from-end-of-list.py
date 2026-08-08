# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count=0
        dummy=head
        while dummy:
            dummy=dummy.next
            count+=1
        if count==n:
            return head.next
        pos=count-n-1
        c=0
        dummy=head
        while dummy:
            if pos==c:
                dummy.next=dummy.next.next
                break
            else:
                c+=1
                dummy=dummy.next
        return head

    
