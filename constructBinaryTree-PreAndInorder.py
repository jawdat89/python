from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])
        return root

# Helper function to print the tree in level order to verify correctness
def print_level_order(root: Optional[TreeNode]):
    if not root:
        return []
    
    queue = [root]
    result = []
    while queue:
        current = queue.pop(0)
        if current:
            result.append(current.val)
            queue.append(current.left)
            queue.append(current.right)
        else:
            result.append(None)
    # Remove trailing Nones for cleaner output
    while result and result[-1] is None:
        result.pop()
    return result

# Test case
preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]
solution = Solution()
root = solution.buildTree(preorder, inorder)

# Expected output: [3, 9, 20, None, None, 15, 7]
print(print_level_order(root))
