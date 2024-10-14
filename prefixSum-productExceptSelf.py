from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in reversed(range(len(nums))):
            res[i] *= postfix
            postfix *= nums[i]

        return res

if __name__ == '__main__':
    s = Solution()
    print(s.productExceptSelf([1, 2, 3, 4]))  # [24, 12, 8, 6]
    print(s.productExceptSelf([-1, 1, 0, -3, 3]))  # [0, 0, 9, 0, 0]
    print(s.productExceptSelf([1, 2, 3, 4, 5]))  # [120, 60, 40, 30, 24]
    print(s.productExceptSelf([1, 2, 3, 4, 5, 6]))  # [720, 360, 240, 180, 144, 120]
    print(s.productExceptSelf([1, 2, 3, 4, 5, 6, 7]))  # [5040, 2520, 1680, 1260, 1008, 840, 720]
    print(s.productExceptSelf([1, 2, 3, 4, 5, 6, 7, 8]))  # [40320, 20160, 13440, 10080, 8064, 6720, 5760, 5040]
    print(s.productExceptSelf([1, 2, 3, 4, 5, 6, 7, 8, 9]))  # [362880, 181440, 120960, 90720, 72576, 60480, 51840, 45360, 40320]
    print(s.productExceptSelf([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))  # [3628800, 1814400, 1209600, 907200, 725760, 604800, 518400, 453600, 403200, 362880]
    print(s.productExceptSelf([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))  # [39916800, 19958400, 13305600, 9979200, 7983360, 6652800, 5702400, 4989600, 4435200, 3991680, 3628800]
    print(s.productExceptSelf([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))  # [479001600, 239500800, 159667200, 119750400, 95800320, 79833600, 68428800, 59875200, 53222400, 47900160, 43545600, 36288000]
