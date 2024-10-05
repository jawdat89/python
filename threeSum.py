from typing import List

class Solution:
  def threeSum(self, nums: List[int]) -> List[List[int]]:
      # Result list to store the triplets
      res = []
      
      # Sort the array to use the two-pointer technique
      nums.sort()

      # Iterate through the array
      for i, n in enumerate(nums):
          # Skip duplicate elements to avoid duplicate triplets
          if i > 0 and n == nums[i - 1]:
              continue

          # Initialize two pointers
          l, r = i + 1, len(nums) - 1

          # Use two-pointer technique to find the other two numbers
          while l < r:
              threeSum = n + nums[l] + nums[r]

              if threeSum > 0:
                  # If the sum is too large, decrease the right pointer
                  r -= 1
              elif threeSum < 0:
                  # If the sum is too small, increase the left pointer
                  l += 1
              else:
                  # If the sum is zero, add the triplet to the result
                  res.append([n, nums[l], nums[r]])
                  
                  # Move the left pointer to the right, skipping duplicates
                  l += 1
                  while l < r and nums[l] == nums[l - 1]:
                      l += 1
              
      return res

# Example usage and test cases
if __name__ == '__main__':
  s = Solution()
  
  # Test case 1: Basic example
  print(s.threeSum([-1, 0, 1, 2, -1, -4]))  # Expected output: [[-1, -1, 2], [-1, 0, 1]]
  
  # Test case 2: All positive numbers
  print(s.threeSum([1, 2, 3, 4, 5]))  # Expected output: []
  
  # Test case 3: All negative numbers
  print(s.threeSum([-5, -4, -3, -2, -1]))  # Expected output: []
  
  # Test case 4: Mixed numbers with multiple solutions
  print(s.threeSum([-2, 0, 1, 1, 2]))  # Expected output: [[-2, 0, 2], [-2, 1, 1]]
  
  # Test case 5: Duplicates in the array
  print(s.threeSum([-2, -2, 0, 0, 2, 2]))  # Expected output: [[-2, 0, 2]]