# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
      if not root or val == root.val:
          return root

      if val > root.val:
          return self.searchBST(root.right, val)
      elif val < root.val:
          return self.searchBST(root.left, val)
      
    def search(self, root, target):
      if not root:
          return False
      
      if target > root.val:
          return self.search(root.right, target)
      elif target < root.val:
          return self.search(root.left, target)
      else:
          return True