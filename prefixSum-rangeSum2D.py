# class NumMatrix:

#     def __init__(self, matrix: List[List[int]]):
#         ROWS, COLS = len(matrix), len(matrix[0])
#         self.prefix = [[0] * COLS for _ in range(ROWS)]

#         for r in range(ROWS):
#             for c in range(COLS):
#                 self.prefix[r][c] = matrix[r][c]

#                 if r:
#                     self.prefix[r][c] += self.prefix[r - 1][c]
#                 if c:
#                     self.prefix[r][c] += self.prefix[r][c - 1]
#                 if r and c:
#                     self.prefix[r][c] -= self.prefix[r - 1][c - 1]
                
#     def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
#         total = self.prefix[row2][col2]

#         if row1:
#             total -= self.prefix[row1 - 1][col2]
#         if col1:
#             total -= self.prefix[row2][col1 - 1]
#         if row1 and col1:
#             total += self.prefix[row1 - 1][col1 - 1] 

#         return total
        


# # Your NumMatrix object will be instantiated and called as such:
# # obj = NumMatrix(matrix)
# # param_1 = obj.sumRegion(row1,col1,row2,col2)

from typing import List

class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        ROWS, COLS = len(matrix), len(matrix[0])
        self.sumMat = [[0] * (COLS + 1) for _ in range(ROWS + 1)]

        for r in range(ROWS):
            prefix = 0
            for c in range(COLS):
                prefix += matrix[r][c]
                above = self.sumMat[r][c + 1]
                self.sumMat[r + 1][c + 1] = prefix + above

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1, c1, r2, c2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1

        bottomRight = self.sumMat[r2][c2]
        above       = self.sumMat[r1 - 1][c2]
        left        = self.sumMat[r2][c1 - 1]
        topLeft     = self.sumMat[r1 - 1][c1 - 1]

        return bottomRight - above - left + topLeft

def main():
    # Example matrix
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    num_matrix = NumMatrix(matrix)

    # Test cases
    test_cases = [
        ((0, 0, 1, 1), 12),  # Sum of submatrix [[1, 2], [4, 5]]
        ((1, 1, 2, 2), 28),  # Sum of submatrix [[5, 6], [8, 9]]
        ((0, 0, 2, 2), 45),  # Sum of the entire matrix
    ]

    for i, (params, expected) in enumerate(test_cases):
        result = num_matrix.sumRegion(*params)
        print(f"Test case {i + 1}: {'Passed' if result == expected else 'Failed'}")
        print(f"Input: {params}, Expected: {expected}, Got: {result}\n")

if __name__ == "__main__":
    main()