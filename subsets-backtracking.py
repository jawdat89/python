# File name: subset_generator.py

from typing import List

class Solution:
    """
    A class to generate all possible subsets of a given list of integers.
    """

    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Generate all possible subsets of the given list of integers.

        This method uses a depth-first search (DFS) approach to generate all subsets.
        It considers each number in the input list and makes two decisions for each:
        include the number in the subset or exclude it.

        Args:
            nums (List[int]): A list of integers.

        Returns:
            List[List[int]]: A list of all possible subsets, where each subset is represented as a list.

        Time complexity: O(2^n), where n is the length of nums.
        Space complexity: O(n) for the recursion stack, O(2^n) for storing all subsets.
        """
        res = []  # List to store all subsets

        subset = []  # Current subset being constructed
        def dfs(i):
            """
            Depth-first search helper function to generate subsets.

            Args:
                i (int): Current index in the nums list being considered.
            """
            # Base case: if we've considered all numbers, add the current subset to the result
            if i >= len(nums):
                res.append(subset.copy())  # Note: we need to create a copy of the subset
                return

            # Decision 1: Include nums[i] in the subset
            subset.append(nums[i])
            dfs(i + 1)  # Recurse to the next index

            # Decision 2: Exclude nums[i] from the subset
            subset.pop()  # Remove the last added element (backtrack)
            dfs(i + 1)  # Recurse to the next index

        # Start the DFS from index 0
        dfs(0)
        return res

def main():
    # Create an instance of the Solution class
    solution = Solution()

    # Test cases
    test_cases = [
        [1, 2, 3],
        [0],
        [1, 2, 3, 4]
    ]

    # Run test cases
    for i, nums in enumerate(test_cases):
        print(f"Test case {i + 1}:")
        print(f"Input: {nums}")
        result = solution.subsets(nums)
        print(f"Output: {result}")
        print(f"Number of subsets: {len(result)}")
        print()

if __name__ == "__main__":
    main()