from typing import List

class Solution:
  def missingNumber(self, nums: List[int]) -> int:
      
      print(f"Input array: {nums}")
      print(f"Searching for missing number in range 0 to {len(nums)}")
      # res = -1
      # for i in range(len(nums) + 1):
      #     print(f"Checking if {i} is in nums...")
      #     if i not in nums:
      #         res = i
      #         print(f"Found missing number: {res}")
      #         break

      res = len(nums)
      for i in range(len(nums)):
          res ^= i ^ nums[i]
          print(f"res: {res}")

      # res = len(nums)
      # for i in range(len(nums)):
      #     res += i - nums[i]
      #     print(f"res: {res}")
      
      return res

      # return len(nums) * (len(nums) + 1) // 2 - sum(nums)

# Test cases
def test_missing_number():
  solution = Solution()
  
  # Test case 1
  nums1 = [3, 0, 1]
  result1 = solution.missingNumber(nums1)
  print(f"Test case 1 result: {result1}\n")
  
  # # Test case 2
  # nums2 = [0, 1]
  # result2 = solution.missingNumber(nums2)
  # print(f"Test case 2 result: {result2}\n")
  
  # # Test case 3
  # nums3 = [9, 6, 4, 2, 3, 5, 7, 0, 1]
  # result3 = solution.missingNumber(nums3)
  # print(f"Test case 3 result: {result3}\n")

# Run the test cases
test_missing_number()