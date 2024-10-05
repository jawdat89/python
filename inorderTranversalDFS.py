# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def inorderHelper(self, root, res):
    #     if not root:
    #         return
    #     self.inorderHelper(root.left, res)
    #     res.append(root.val)
    #     self.inorderHelper(root.right, res)

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # res = []
        # def inorderHelper(root):
        #     if not root:
        #         return
        #     inorderHelper(root.left)
        #     res.append(root.val)
        #     inorderHelper(root.right)

        # inorderHelper(root)
        # return res

        res = []
        if not root:
            return res
        stack = []
        cur = root
        while len(stack) != 0 or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right
        return res



        