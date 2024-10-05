class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        # l, r = 0, 1 # left=buy, right= sell
        # maxP = 0

        # while r < len(prices):
        #     if prices[l] < prices[r]:
        #         maxP = max(maxP, prices[r] - prices[l])
        #     else:
        #         l = r
        #     r += 1
        # return maxP

        l, maxP = 0, 0
        for r in range(1, len(prices)):
            if prices[r] < prices[l]:
                l = r
            else:
                maxP = max(maxP, prices[r] - prices[l])

        return maxP
