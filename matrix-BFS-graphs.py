from collections import deque

# Matrix (2D Grid)
grid = [[0, 0, 0, 0],
        [1, 1, 0, 0],
        [0, 0, 0, 1],
        [0, 1, 0, 0]]

# Shortest path from top left to bottom right
def bfs(grid):
    rows, cols = len(grid), len(grid[0])
    visit = set()
    queue = deque()
    queue.append((0, 0))
    visit.add((0, 0))

    length = 0
    while queue:
        for i in range(len(queue)):
            r, c = queue.popleft()
            if r == rows - 1 and c == cols - 1:
                return length

            neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in neighbors:
                rx, cx = r + dr, c + dc
                if (min(rx, cx) < 0 or
                    rx == rows or cx == cols or
                    (rx, cx) in visit or grid[rx][cx] == 1):
                    continue
                queue.append((rx, cx))
                visit.add((rx, cx))
        length += 1

    return -1  # Return -1 if there is no path
