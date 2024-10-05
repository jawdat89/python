class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Brute Force
        # res = 0
        
        # for l in range(len(heights)):
        #     for r in range(l + 1, len(heights)):
        #         area = (r - l) * min(heights[l], heights[r])
        #         res = max(res, area)
        # return res

        L, R = 0, len(heights) - 1
        res = 0

        while L < R:
            area = (R - L) * min(heights[L], heights[R])
            if heights[L] < heights[R]:
                L += 1
            else:
                R -= 1
                
            res = max(res, area)

        return res
