# File name: combination_sum.py

from typing import List

class Solution:
  def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
      """
      Find all unique combinations in candidates where the candidate numbers sum to target.

      Args:
      candidates (List[int]): A list of distinct positive integers.
      target (int): The target sum.

      Returns:
      List[List[int]]: A list of all unique combinations that sum to target.
      """
      res = []
      
      def dfs(i: int, cur: List[int], remain: int):
          if remain == 0:
              res.append(cur.copy())
              return
          if i >= len(nums) or remain < 0:
              return
          
          # Include the current candidate
          cur.append(nums[i])
          dfs(i, cur, remain - nums[i])
          
          # Don't include the current candidate
          cur.pop()
          dfs(i + 1, cur, remain)
      
      dfs(0, [], target)

      # def dfs(i, cur, total):
      #       if total == target:
      #           res.append(cur.copy())
      #           return
      #       if i >= len(nums) or total > target:
      #           return

      #       cur.append(nums[i])
      #       dfs(i, cur, total + nums[i])
      #       cur.pop()
      #       dfs(i + 1, cur, total)
        
      # dfs(0, [], 0)
      
      return res

def main():
  # Create an instance of the Solution class
  solution = Solution()

  # Test cases
  test_cases = [
      ([2, 3, 6, 7], 7),
      ([2, 3, 5], 8),
      ([2], 1),
      ([1], 1),
      ([1], 2)
  ]

  # Run test cases
  for i, (candidates, target) in enumerate(test_cases):
      print(f"Test case {i + 1}:")
      print(f"Candidates: {candidates}")
      print(f"Target: {target}")
      result = solution.combinationSum(candidates, target)
      print(f"Output: {result}")
      print(f"Number of combinations: {len(result)}")
      print()

if __name__ == "__main__":
  main()