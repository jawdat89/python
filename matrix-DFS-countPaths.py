from typing import List


class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        ROWS, COLS = len(grid), len(grid[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visit = set()

        def dfs(r, c):
            if (min(r, c) < 0 or r == ROWS or c == COLS or
                grid[r][c] == 1 or (r, c) in visit):
                return 0

            if r == ROWS - 1 and c == COLS - 1:
                return 1

            visit.add((r, c))
            count = 0
            for dr, dc in directions:
                count += dfs(r + dr, c + dc)
            # count = 0
            # count += dfs(r + 1, c)
            # count += dfs(r - 1, c)
            # count += dfs(r, c + 1)
            # count += dfs(r, c - 1)

            
            visit.remove((r,c))

            return count

        return dfs(0,0)

# Example usage
if __name__ == "__main__":
    solution = Solution()
    grid = [
        [0, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 1],
        [0, 1, 0, 0]
    ]
    print("Number of islands:", solution.countPaths(grid))  # Expected Output: 3