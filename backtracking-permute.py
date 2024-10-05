class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # def helper(i, nums):
        #     if i == len(nums):
        #         return [[]]

        #     resPerms = []
        #     perms = helper(i + 1, nums)
        #     for p in perms:
        #         for j in range(len(p) + 1):
        #             pCopy = p.copy()
        #             pCopy.insert(j, nums[i])
        #             resPerms.append(pCopy)
        #     return resPerms
        # return helper(0, nums)

        perms = [[]]

        for n in nums:
            nextPerms = []
            for p in perms:
                for i in range(len(p) + 1):
                    pCopy = p.copy()
                    pCopy.insert(i, n)
                    nextPerms.append(pCopy)
            perms = nextPerms
        return perms
    