# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # if not root:
        #     return 0
        # q = deque([root])
        # length = 0
        # while q:
        #     for i in range(len(q)):
        #         cur = q.popleft()

        #         if cur.left:
        #             q.append(cur.left)
        #         if cur.right:
        #             q.append(cur.right)
        #     length += 1

        # return length

        # if not root:
        #     return 0

        # stack = [[root, 1]]

        # res = 0

        # while stack:
        #     cur, depth = stack.pop()

        #     res = max(res, depth)

        #     if cur.left:
        #         stack.append([cur.left, depth + 1])
        #     if cur.right:
        #         stack.append([cur.right, depth + 1])

        # return res

        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))