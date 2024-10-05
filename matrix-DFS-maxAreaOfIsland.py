class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        ROWS, COLS = len(grid), len(grid[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visit = set()

        def dfs(r, c):
            if (min(r, c) < 0 or r == ROWS or c == COLS or
                grid[r][c] == 0 or (r, c) in visit):
                return 0 

            visit.add((r, c))
            # return (
            #         1 + dfs(r + 1, c) +
            #             dfs(r - 1, c) +
            #             dfs(r, c + 1) +
            #             dfs(r, c - 1)
            #             )
            land = 1
            for dr, dc in directions:
                land += dfs(r + dr, c + dc)

            return land

        count = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visit:
                    count = max(count, dfs(r, c))
        return count