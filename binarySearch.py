from typing import List
# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    return False if version < 4 else True

class Solution:

    # Python implementation of Binary Search
    def binarySearch(arr, target):
        L, R = 0, len(arr) - 1

        while L <= R:
            # m = L + ((R - L) // 2) # mid point garantueed to be in the range of L and R
            m = (L + R) // 2


            if target > arr[m]:
                L = m + 1
            elif target < arr[m]:
                R = m - 1
            else:
                return m
        return -1

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        # m, n = len(matrix), len(matrix[0])
        # L, R = 0, m * n - 1

        # while L <= R:
        #     m = (L + R) // 2
        #     m_val = matrix[m // n][m % n]  # Corrected line

        #     if target > m_val:
        #         L = m + 1
        #     elif target < m_val:
        #         R = m - 1
        #     else:
        #         return True
        
        # return False

        ROWS, COLS = len(matrix), len(matrix[0])
        top, bot = 0, ROWS - 1

        while top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break
        
        if not top <= bot:
            return False
        
        row = (top + bot) // 2
        l, r = 0, COLS - 1
        while l <= r:
            m = (l + r) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        
        return False

    def firstBadVersion(self, n: int) -> int:
        l, r = 1, n

        while l < r:
            m = (l + r) // 2

            if isBadVersion(m):
                r = m
            else:
                l = m + 1

        return l

solution = Solution()

# Example for running a single test case
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 16
print(f"Test Case 1: {solution.searchMatrix(matrix, target)}")  # Expected: True

# Repeat for other test cases...
