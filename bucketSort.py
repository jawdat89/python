from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        counts = [0, 0, 0]  # Initialize counts for red, white, and blue
        for n in nums:
            counts[n] += 1  # Count occurrences of each color

        i = 0
        for n in range(len(counts)):
            for j in range(counts[n]):
                nums[i] = n
                i += 1

def print_colors(nums):
    colors = ['Red', 'White', 'Blue']
    return [colors[num] for num in nums]

# Instantiate Solution
solution = Solution()

# Test Case 1: Mixed Colors
nums1 = [2, 0, 2, 1, 1, 0]
solution.sortColors(nums1)
print(f"Test Case 1: {print_colors(nums1)}")

# Test Case 2: All One Color
nums2 = [1, 1, 1, 1]
solution.sortColors(nums2)
print(f"Test Case 2: {print_colors(nums2)}")

# Test Case 3: Empty List
nums3 = []
solution.sortColors(nums3)
print(f"Test Case 3: {print_colors(nums3)}")

# Test Case 4: Single Color Variations
nums4 = [0, 2, 2, 2, 1, 0]
solution.sortColors(nums4)
print(f"Test Case 4: {print_colors(nums4)}")

# Test Case 5: Already Sorted
nums5 = [0, 0, 1, 1, 2, 2]
solution.sortColors(nums5)
print(f"Test Case 5: {print_colors(nums5)}")

# Test Case 6: Reverse Order
nums6 = [2, 2, 1, 1, 0, 0]
solution.sortColors(nums6)
print(f"Test Case 6: {print_colors(nums6)}")
