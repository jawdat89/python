from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow

        # If no duplicate is found, which shouldn't happen given the problem constraints


# Test cases
def test_duplicate_number():
    solution = Solution()

    # Test case 1
    nums1 = [1, 3, 4, 2, 2]
    result1 = solution.findDuplicate(nums1)
    print(f"Test case 1 result: {result1}\n")

    # Test case 2
    nums2 = [3, 1, 3, 4, 2]
    result2 = solution.findDuplicate(nums2)
    print(f"Test case 2 result: {result2}\n")

    # Test case 3
    nums3 = [1, 1]
    result3 = solution.findDuplicate(nums3)
    print(f"Test case 3 result: {result3}\n")

    # Test case 4
    nums4 = [1, 1, 2]
    result4 = solution.findDuplicate(nums4)
    print(f"Test case 4 result: {result4}\n")

if __name__ == "__main__":
    test_duplicate_number()