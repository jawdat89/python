from collections import deque
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visit = set()

        q = deque()
        def bfs(r, c):
            q.append((r, c))
            visit.add((r, c))

            while q:
                row, col = q.popleft()

                for dr, dc in directions:
                    rx, cx = row + dr, col + dc

                    if (rx in range(ROWS) and cx in range(COLS) and
                        grid[rx][cx] == '1' and (rx, cx) not in visit):
                        q.append((rx, cx))
                        visit.add((rx, cx))

        islands = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1' and (r, c) not in visit:
                    bfs(r,c)
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