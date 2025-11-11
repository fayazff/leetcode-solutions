# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        curr=dummy
        carry=0
        p,q=l1,l2
        while p is not None or q is not None or carry:
            x=p.val if p is not None else 0
            y=q.val if q is not None else 0
            total=x+y+carry
            digit=total%10
            carry=total//10

            curr.next=ListNode(digit)
            curr=curr.next

            if p is not None:
                p=p.next
            if q is not None:
                q=q.next
        return dummy.next 
