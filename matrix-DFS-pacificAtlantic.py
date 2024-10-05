from typing import List

class Solution:
  def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
      # Get the number of rows and columns in the grid
      ROWS, COLS = len(heights), len(heights[0])
      
      # Define the possible directions for movement (right, left, down, up)
      directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
      
      # Sets to keep track of cells that can reach the Pacific and Atlantic oceans
      pac, atl = set(), set()

      def dfs(r, c, visit, prevHeight):
          # Base case: check if the current cell is out of bounds, already visited, or lower than the previous cell
          if (min(r, c) < 0 or r == ROWS or c == COLS or
              (r, c) in visit or heights[r][c] < prevHeight):
              return
          
          # Mark the current cell as visited
          visit.add((r, c))
          
          # Explore all four directions
          for dr, dc in directions:
              dfs(r + dr, c + dc, visit, heights[r][c])

      # Perform DFS from the Pacific Ocean (top and left edges)
      for c in range(COLS):
          dfs(0, c, pac, heights[0][c])  # Top edge
          dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])  # Bottom edge

      # Perform DFS from the Atlantic Ocean (bottom and right edges)
      for r in range(ROWS):
          dfs(r, 0, pac, heights[r][0])  # Left edge
          dfs(r, COLS - 1, atl, heights[r][COLS - 1])  # Right edge

      # Collect cells that can reach both oceans
      res = []
      for r in range(ROWS):
          for c in range(COLS):
              if (r, c) in pac and (r, c) in atl:
                  res.append([r, c])

      return res