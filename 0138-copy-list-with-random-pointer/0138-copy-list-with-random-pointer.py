"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        temp=head
        if temp==None:
            return None
        # Step 1: Insert copied nodes after each original node
        while temp!=None:
            node=Node(temp.val)
            node.next=temp.next
            temp.next=node
            temp=node.next
        head2=head.next
        # Step 2: Assign random pointers
        temp=head
        while temp!=None:
            if temp.random!=None:
                temp.next.random=temp.random.next
            temp=temp.next.next
        # Step 3: Separate the two lists
        temp=head
        temp2=head2
        while temp!=None:
            temp.next=temp2.next
            if temp2.next!=None:
                temp2.next=temp.next.next
            temp=temp.next
            temp2=temp2.next
        return head2


            
