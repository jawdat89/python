# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        queue = deque()

        if root:
            queue.append(root)

        res = []
        while len(queue) > 0:
            level_size = len(queue)
            level = []
            for i in range(level_size)):
                cur = queue.popleft()
                level.append(cur.val)

                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
                
            res.append(level)
        return res