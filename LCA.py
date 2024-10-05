# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right

class Solution:
  def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
      cur = root

      while cur:
          if p.val > cur.val and q.val > cur.val:
              cur = cur.right
          elif p.val < cur.val and q.val < cur.val:
              cur = cur.left
          else:
              return cur

# Utility function to create a binary search tree
def create_bst():
  # Constructing the BST:
  #         6
  #        / \
  #       2   8
  #      / \ / \
  #     0  4 7  9
  #       / \
  #      3   5
  root = TreeNode(6)
  root.left = TreeNode(2)
  root.right = TreeNode(8)
  root.left.left = TreeNode(0)
  root.left.right = TreeNode(4)
  root.right.left = TreeNode(7)
  root.right.right = TreeNode(9)
  root.left.right.left = TreeNode(3)
  root.left.right.right = TreeNode(5)
  return root

# Example usage
if __name__ == '__main__':
  # Create the BST
  root = create_bst()

  # Define nodes p and q
  p = root.left.left  # Node with value 0
  q = root.right.right  # Node with value 9

  # Find the LCA
  solution = Solution()
  lca = solution.lowestCommonAncestor(root, p, q)

  # Print the result
  print(f"The LCA of nodes {p.val} and {q.val} is: {lca.val}")  # Expected output: 6