# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:        
        # if not subRoot:
        #     return True

        # def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #   if not p and not q:
        #       return True
        #   if not p or not q:
        #       return False
        #   return (p.val == q.val and 
        #           isSameTree(p.left, q.left) and isSameTree(p.right, q.right))

        # q = deque()
        # if root:
        #     q.append(root)

        # while q:
        #     for i in range(len(q)):
        #         cur = q.popleft()

        #         if isSameTree(cur, subRoot):
        #           return True
                
        #         if cur.left:
        #             q.append(cur.left)
        #         if cur.right:
        #             q.append(cur.right)

        # return False

        if not subRoot:
            return True
        if not root:
            return False

        if self.sameTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def sameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        if root and subRoot and root.val == subRoot.val:
            return self.sameTree(root.left, subRoot.left) and self.sameTree(root.right, subRoot.right)
        return False