from typing import List

class Solution:
  def findMin(self, nums: List[int]) -> int:
      # If the array contains only one element, return that element
      if len(nums) == 1:
          return nums[0]

      # Initialize the result with positive infinity
      res = float('inf')

      # Set the left and right pointers for binary search
      l, r = 0, len(nums) - 1

      # Perform binary search
      while l <= r:
          # Check if the current subarray is already sorted
          if nums[l] < nums[r]:
              # If sorted, the minimum is the leftmost element
              return min(res, nums[l])

          # Calculate the middle index
          m = (l + r) // 2

          # Update the result with the minimum value found so far
          res = min(res, nums[m])

          # Check if the left half is sorted
          if nums[m] >= nums[l]:
              # If the left half is sorted, the minimum must be in the right half
              # Move the left pointer to the right of the middle
              l = m + 1
          else:
              # If the left half is not sorted, the minimum must be in the left half
              # Move the right pointer to the left of the middle
              r = m - 1

      # Return the minimum value found
      return res

# Test cases
def test_findMin():
  solution = Solution()

  # Test case 1: Simple rotated array
  nums1 = [4, 5, 6, 7, 0, 1, 2]
  print(f"Test case 1: {nums1} -> Minimum: {solution.findMin(nums1)}")  # Expected output: 0

  # Test case 2: Array rotated at the middle
  nums2 = [3, 4, 5, 1, 2]
  print(f"Test case 2: {nums2} -> Minimum: {solution.findMin(nums2)}")  # Expected output: 1

  # Test case 3: Array not rotated (sorted)
  nums3 = [1, 2, 3, 4, 5, 6, 7]
  print(f"Test case 3: {nums3} -> Minimum: {solution.findMin(nums3)}")  # Expected output: 1

  # Test case 4: Single element array
  nums4 = [10]
  print(f"Test case 4: {nums4} -> Minimum: {solution.findMin(nums4)}")  # Expected output: 10

  # Test case 5: Two elements, rotated
  nums5 = [2, 1]
  print(f"Test case 5: {nums5} -> Minimum: {solution.findMin(nums5)}")  # Expected output: 1

  # Test case 6: Large array with rotation
  nums6 = [15, 18, 2, 3, 6, 12]
  print(f"Test case 6: {nums6} -> Minimum: {solution.findMin(nums6)}")  # Expected output: 2

  # Test case 7: Array with duplicates
  nums7 = [2, 2, 2, 0, 1]
  print(f"Test case 7: {nums7} -> Minimum: {solution.findMin(nums7)}")  # Expected output: 0

  # Test case 8: Array with all identical elements
  nums8 = [3, 3, 3, 3, 3]
  print(f"Test case 8: {nums8} -> Minimum: {solution.findMin(nums8)}")  # Expected output: 3

if __name__ == '__main__':
  test_findMin()