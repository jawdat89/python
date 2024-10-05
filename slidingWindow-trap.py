from typing import List


class Solution:
    # O(1) solution
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        L, R = 0, len(height) - 1
        maxL, maxR = height[L], height[R]

        res = 0

        while L < R:
            if maxL < maxR:
                L += 1
                maxL = max(maxL, height[L])
                res += maxL - height[L]
            else:
                R -= 1
                maxR = max(maxR, height[R])
                res += maxR - height[R]

        return res
    
    # O(n) solution
    def trapOn(self, height: List[int]) -> int:
        if not height:
            return 0
        n = len(height)
        maxL = [0] * n
        maxR = [0] * n
         # Fill maxL array
        maxL[0] = height[0]
        for i in range(1, n):
            maxL[i] = max(maxL[i - 1], height[i])

        # Fill maxR array
        maxR[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            maxR[i] = max(maxR[i + 1], height[i])

        # Calculate the trapped water
        res = 0
        for i in range(n):
            res += min(maxL[i], maxR[i]) - height[i]

        return res


if __name__ == '__main__':
    s = Solution()
    print(s.trap([0,2,0,3,1,0,1,3,2,1])) # 9
    print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1])) # 6
    print(s.trap([4,2,0,3,2,5])) # 9
    print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1])) # 6
    print(s.trap([4,2,0,3,2,5])) # 9
    print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1])) # 6
    print(s.trap([4,2,0,3,2,5])) # 9
    print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1])) # 6
    print(s.trap([4,2,0,3,2,5])) # 9
    print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1])) # 6
    print(s.trap([4,2,0,3,2,5])) # 9
    print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1])) # 6
    print(s.trap([4,2,0,3,2,5])) # 9
    print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1])) # 6
    print(s.trap([4,2,0,3,2,5])) # 9
    print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1])) # 6
    print(s.trap([4,2,0,3,2,5])) # 9
    print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1])) # 6