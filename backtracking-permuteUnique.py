class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # perms = [[]]

        # for n in nums:
        #     nextPerms = []
        #     for p in perms:
        #         for i in range(len(p) + 1):
        #             pCopy = p.copy()
        #             pCopy.insert(i, n)
        #             if pCopy not in nextPerms:
        #                 nextPerms.append(pCopy)
        #     perms = nextPerms
        # return perms
        
        res = []
        perm = []

        count = Counter(nums)
    
        def dfs():
            if len(perm) == len(nums):
                res.append(perm.copy())
                return

            for n in count:
                if count[n] > 0:
                    perm.append(n)
                    count[n] -= 1

                    dfs()

                    count[n] += 1
                    perm.pop()
            
        dfs()

        return res
