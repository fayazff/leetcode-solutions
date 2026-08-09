# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dumy=head
        count=0
        while dumy:
            count+=1
            dumy=dumy.next
        if count==n:
            return head.next
        k=count-n-1
        dumy=head
        c=0
        while dumy:
            if c==k:
                dumy.next=dumy.next.next
                dumy=dumy.next
                break
            else:
                dumy=dumy.next
                c+=1
        return head

