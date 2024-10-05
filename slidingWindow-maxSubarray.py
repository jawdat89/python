class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums: return 0
        maxSum = nums[0] 
        curSum = 0
        
        for n in nums:
            curSum = max(curSum, 0)
            curSum += n
            maxSum = max(maxSum, curSum)

        return maxSum
