import heapq
from typing import List


class Solution:
    class Solution:
        def findKthLargest(self, nums: List[int], k: int) -> int:
            def heapifysolution(nums, k):
                res = -1
                if not nums:
                    return res

                negated_nums = [-num for num in nums]

                heapq.heapify(negated_nums)

                while k > 0:
                    res = -heapq.heappop(negated_nums)
                    k -= 1
            
                return res
            # def numsSortSolution(nums, k):
            #     if not nums or len(nums) - k < 0:
            #         return -1
            #     nums.sort()
            #     return nums[len(nums)-k]
            
            def quickSelectSolution(nums, k):
                k = len(nums) - k

                def quickSelect(l, r):
                    pivot, p = nums[r], l
                    for i in range(l, r):
                        if nums[i] <= pivot:
                            nums[p], nums[i] = nums[i], nums[p]
                            p += 1
                    nums[p], nums[r] = nums[r], nums[p]

                    if p > k:   return quickSelect(l, p - 1)
                    elif p < k: return quickSelect(p + 1, r)
                    else:       return nums[p]
                return quickSelect(0, len(nums) - 1)
            
            # The soultion choice
            return quickSelectSolution(nums, k)

if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1
    print("Test Case 1:", solution.findKthLargest([3, 2, 1, 5, 6, 4], 2))  # Expected Output: 5
    
    # Test Case 2
    print("Test Case 2:", solution.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))  # Expected Output: 4

    # Test Case 3
    print("Test Case 3:", solution.findKthLargest([1], 1))  # Expected Output: 1
    
    # Test Case 4
    print("Test Case 4:", solution.findKthLargest([5, 6, 4, 3, 2, 1], 6))  # Expected Output: 1
    
    # Test Case 5
    print("Test Case 5:", solution.findKthLargest([1, 2, 3, 4, 5, 6], 1))  # Expected Output: 6
