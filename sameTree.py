# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        
        # queue = deque([[p, q]])

        # while queue:
        #     for i in range(len(queue)):
        #         p, q = queue.popleft()

        #         if p.val != q.val:
        #             return False

        #         if ((p.left and not q.left) or 
        #            (not p.left and q.left) or
        #            (p.right and not q.right) or
        #            (not p.right and q.right)):
        #            return False 

        #         if p.left and q.left:
        #             queue.append([p.left, q.left])
        #         if p.right and q.right:
        #             queue.append([p.right, q.right])
        
        # return True

        if p.val != q.val:
            return False        
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    

        # short version
        def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
          if not p and not q:
              return True
          if not p or not q or p.val != q.val:
              return False

          return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)