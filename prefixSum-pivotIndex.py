class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if not nums:
            return -1

        totalSum = sum(nums)
        leftSum  = 0

        for i, n in enumerate(nums):
            rightSum = totalSum - leftSum - n
            if leftSum == rightSum:
                return i
            
            leftSum += n

        return -1