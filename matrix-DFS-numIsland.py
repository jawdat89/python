from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        ROWS, COLS = len(grid), len(grid[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visit = set()
        islands = 0

        def dfs(r, c):
            if (min(r, c) < 0 or r == ROWS or c == COLS or
                grid[r][c] == '0' or (r,c) in visit):
                return

            visit.add((r, c))

            for dr, dc in directions:
                dfs(r + dr, c + dc)

        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1' and (r, c) not in visit:
                    dfs(r, c)
                    islands += 1
        return islands


# Example usage
if __name__ == "__main__":
    solution = Solution()
    grid = [
        ["0","1","1","1","0"],
        ["0","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]
    print("Number of islands:", solution.numIslands(grid))  # Expected Output: 1