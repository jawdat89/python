from typing import List

class Solution:
  def maxSubarraySumCircular(self, nums: List[int]) -> int:
      globMax, globMin = nums[0], nums[0]
      curMax, curMin = 0, 0
      total = 0

      for n in nums:
          curMax = max(curMax + n, n)
          curMin = min(curMin + n, n)

          total += n

          globMax = max(globMax, curMax)
          globMin = min(globMin, curMin)

      return max(globMax, total - globMin) if globMax > 0 else globMax

def main():
  solution = Solution()

  # Test cases
  test_cases = [
      ([1, -2, 3, -2], 3),  # Normal case
      ([5, -3, 5], 10),     # Circular case
      ([-3, -2, -3], -2),   # All negative numbers
      ([3, -1, 2, -1], 4),  # Mixed numbers
      ([3, -2, 2, -3], 3),  # Edge case
  ]

  for i, (nums, expected) in enumerate(test_cases):
      result = solution.maxSubarraySumCircular(nums)
      print(f"Test case {i + 1}: {'Passed' if result == expected else 'Failed'}")
      print(f"Input: {nums}, Expected: {expected}, Got: {result}\n")

if __name__ == "__main__":
  main()