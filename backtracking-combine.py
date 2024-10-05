class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def helper(i, curComb, combs, n, k):
            # if len(curComb) == k:
            #     combs.append(curComb.copy())
            #     return
            # if i > n:
            #     return
            # curComb.append(i)
            # helper(i + 1, curComb, combs, n, k)
            # curComb.pop()
            # helper(i + 1, curComb, combs, n, k)
            if len(curComb) == k:
                combs.append(curComb.copy())
                return
            if i > n:
                return

            for j in range(i, n + 1):
                curComb.append(j)
                helper(j + 1, curComb, combs, n, k)
                curComb.pop()

        combs = []
        helper(1, [], combs, n, k)
        
        return combs

