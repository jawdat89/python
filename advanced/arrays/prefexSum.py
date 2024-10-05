class PrefixSum:

    def __init__(self, nums):
        self.prefix = []
        self.postfix = []

        # prefix sum
        total = 0
        for n in nums:
            total += n
            self.prefix.append(total)

        # postfix sum
        total = 0
        for i in reversed(range(len(nums))):
            total += nums[i]
            self.postfix.append(total)
            
    def rangeSum(self, left, right):
        preRight = self.prefix[right]
        preLeft = self.prefix[left - 1] if left > 0 else 0
        return (preRight - preLeft)
    
    def reversedSum(self, left, right):
        postLeft = self.postfix[left]
        postRight = self.postfix[right + 1] if right + 1 < len(self.postfix) else 0
        return postLeft - postRight
