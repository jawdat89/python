from collections import deque
from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        N = len(grid)
        q = deque([(0, 0, 1)]) # (r, c, length)
        visit = set((0, 0))
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0],
                      [1, 1], [1, -1], [-1,1], [-1,-1]] # 8-directionally
        
        while q:
            for i in range(len(q)):
                r, c, length = q.popleft()
                if (min(r, c) < 0 or max(r, c) >= N or
                    grid[r][c] == 1):
                    continue
                if r == N - 1 and c == N - 1:
                    return length

                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if (row, col) not in visit:
                        q.append((row, col, length + 1))
                        visit.add((row, col))

        return -1
