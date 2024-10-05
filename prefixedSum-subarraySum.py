from typing import List

class Solution:
  def subarraySum(self, nums: List[int], k: int) -> int:
      res = 0
      curSum = 0
      prefixSums = {0: 1}  # Initialize with 0:1 to handle subarrays starting from index 0

      for n in nums:
          curSum += n  # Update the cumulative sum with the current number

          diff = curSum - k  # Calculate the difference needed to form a subarray sum of k

          # If the difference exists in prefixSums, it means there is a subarray 
          # ending at the current index
          # which sums to k. Add the count of such subarrays to the result.
          res += prefixSums.get(diff, 0)

          # Update the prefixSums with the current cumulative sum
          # If curSum is already in prefixSums, increment its count;
          # otherwise, set it to 1.
          prefixSums[curSum] = 1 + prefixSums.get(curSum, 0)

      return res

def main():
  solution = Solution()

  # Test cases with expected results
  test_cases = [
      ([1, 1, 1], 2, 2),  # Expected output: 2
      ([1, 2, 3], 3, 2),  # Expected output: 2
      ([1, -1, 0], 0, 3), # Expected output: 3
      ([3, 4, 7, 2, -3, 1, 4, 2], 7, 4), # Expected output: 4
  ]

  for i, (nums, k, expected) in enumerate(test_cases):
      result = solution.subarraySum(nums, k)
      print(f"Test case {i + 1}: {'Passed' if result == expected else 'Failed'}")
      print(f"Input: nums={nums}, k={k}, Expected: {expected}, Got: {result}\n")

if __name__ == "__main__":
  main()