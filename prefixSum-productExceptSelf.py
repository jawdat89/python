from typing import List

class prefixNums:
  # def __init__(self, nums):
  #     self.prefix = []
  #     self.postfix = []

  #     prefix = 1
  #     for i in range(len(nums)):
  #         prefix *= nums[i]
  #         self.prefix.append(prefix)

  #     postfix = 1
  #     for i in reversed(range(len(nums))):
  #         postfix *= nums[i]
  #         self.postfix.append(postfix)
  #     self.postfix.reverse()

  # def getProduct(self, i):
  #     if i == 0:
  #         return self.postfix[i + 1]
  #     elif i == len(self.prefix) - 1:
  #         return self.prefix[i - 1]
  #     else:
  #         return self.prefix[i - 1] * self.postfix[i + 1]
  def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in reversed(range(len(nums))):
            res[i] *= postfix
            postfix *= nums[i]

        return res

class Solution:
  def productExceptSelf(self, nums: List[int]) -> List[int]:
      prefixed = prefixNums(nums)
      res = []
      for i in range(len(nums)):
          res.append(prefixed.getProduct(i))

      return res

# Example usage
solution = Solution()
print(solution.productExceptSelf([1, 2, 3, 4]))  # Output: [24, 12, 8, 6]