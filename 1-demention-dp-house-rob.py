from typing import List

class Solution:
  def rob(self, nums: List[int]) -> int:
      # Initialize two variables to keep track of the maximum money robbed
      # up to the previous two houses.
      rob1, rob2 = 0, 0

      # Iterate over each house in the list.
      # [rob1, rob2, n, n+1, ...] represents the maximum money robbed up to
      # the current house and the previous house.
      for n in nums:
          # Calculate the maximum money that can be robbed by either:
          # 1. Robbing the current house and adding its money to rob1 (money robbed up to two houses before).
          # 2. Skipping the current house and taking rob2 (money robbed up to the previous house).
          temp = max(n + rob1, rob2)
          
          # Update rob1 to be rob2 for the next iteration (shift the window).
          rob1 = rob2
          
          # Update rob2 to be the new maximum money robbed up to the current house.
          rob2 = temp

      # Return the maximum money that can be robbed, which is stored in rob2.
      return rob2
  
def main():
  # Create an instance of the Solution class
  solution = Solution()

  # Test cases
  test_cases = [
      [1, 2, 3, 1],
      [2, 7, 9, 3, 1],
      [2, 1, 1, 2]
  ]

  for nums in test_cases:
      print(solution.rob(nums))

if __name__ == "__main__":
    main()