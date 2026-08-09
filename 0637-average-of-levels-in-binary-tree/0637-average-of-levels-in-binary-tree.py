# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    from collections import deque
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return root
        res=[]
        queue=deque([root])
        
        while queue:
            level=[]
            sums=0
            levl_size=len(queue)
            for _ in range(levl_size):
                node=queue.popleft()
                level.append(node.val)
                sums+=node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
            avg=sums/levl_size
            res.append(avg)
        return res
