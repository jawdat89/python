# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque()

        if root:
            queue.append(root)

        res = []
        while len(queue) > 0:
            level_size = len(queue)
            rightmost_value = None
            
            for i in range(level_size):
                cur = queue.popleft()
                rightmost_value = cur.val

                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            res.append(rightmost_value)
        return res