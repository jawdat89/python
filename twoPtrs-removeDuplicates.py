class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # l = 1

        # for r in range(1, len(nums)):
        #     if nums[r] != nums[r - 1]:
        #         nums[l] = nums[r]
        #         l += 1

        # return l

        # k = 1

        # for i in range(1, len(nums)):
        #     if nums[i] != nums[i - 1]:
        #         nums[k] = nums[i]
        #         k += 1
        # return k

            
        l = 0
        last = None
        for r, n in enumerate(nums):
            if n == last: continue
            last = n
            nums[l] = n
            l += 1
        return l