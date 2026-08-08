# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left=ListNode()
        right=ListNode()
        rightlt=right
        leftlt=left
        while head:
            if head.val < x:
                leftlt.next=head
                leftlt=leftlt.next
            else:
                rightlt.next=head
                rightlt=rightlt.next
            head=head.next
        leftlt.next=right.next
        rightlt.next=None
        return left.next
