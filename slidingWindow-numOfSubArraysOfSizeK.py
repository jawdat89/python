# class PrefixSum:

#     def __init__(self, nums):
#         self.prefix = []
#         total = 0
#         for n in nums:
#             total += n
#             self.prefix.append(total)

#     def rangeSum(self, left, right):
#         preRight = self.prefix[right]
#         preLeft  = self.prefix[left - 1] if left > 0 else 0
#         return (preRight - preLeft)

from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        # L = 0
        # prefixed = PrefixSum(arr)
        # res = 0

        # for R, n in enumerate(arr):
        #     if R - L + 1 > k:
        #         L += 1
            
        #     if R - L + 1 == k:
        #         avg = prefixed.rangeSum(L, R) / k
        #         if avg >= threshold:
        #             res += 1
            
        
        # return res

        res = 0

        curSum = sum(arr[:k-1])

        for L in range(len(arr) - k + 1):
            curSum += arr[L + k - 1]

            if (curSum / k) >= threshold:
                res += 1
            
            curSum -= arr[L]

        return res
    
if __name__ == '__main__':
    s = Solution()
    print(s.numOfSubarrays([2,2,2,2,5,5,5,8], 3, 4)) # 3
    print(s.numOfSubarrays([1,1,1,1,1], 1, 0)) # 5
    print(s.numOfSubarrays([11,13,17,23,29,31,7,5,2,3], 3, 5)) # 6
    print(s.numOfSubarrays([7,7,7,7,7,7,7], 7, 7)) # 1
    print(s.numOfSubarrays([4,4,4,4], 4, 1)) # 1
    print(s.numOfSubarrays([4,4,4,4], 4, 2)) # 1
    print(s.numOfSubarrays([4,4,4,4], 4, 3)) # 1
    print(s.numOfSubarrays([4,4,4,4], 4, 4)) # 1
    print(s.numOfSubarrays([4,4,4,4], 4, 5)) # 0
    print(s.numOfSubarrays([4,4,4,4], 4, 6)) # 0
    print(s.numOfSubarrays([4,4,4,4], 4, 7)) # 0
    print(s.numOfSubarrays([4,4,4,4], 4, 8)) # 0
    print(s.numOfSubarrays([4,4,4,4], 4, 9)) # 0
    print(s.numOfSubarrays([4,4,4,4], 4, 10)) # 0
    print(s.numOfSubarrays([4,4,4,4], 4, 11)) # 0
    print(s.numOfSubarrays([4,4,4,4], 4, 12)) # 0
    print(s.numOfSubarrays([4,4,4,4], 4, 13)) # 0
    print(s.numOfSubarrays([4,4,4,4], 4, 14)) # 0

