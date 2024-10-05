from collections import deque
from typing import List

class Solution:
  def orangesRotting(self, grid: List[List[int]]) -> int:
      """
      Determines the minimum time required for all fresh oranges to become rotten.
      
      Args:
      grid (List[List[int]]): A 2D grid where:
          - 0 represents an empty cell,
          - 1 represents a fresh orange,
          - 2 represents a rotten orange.
      
      Returns:
      int: The minimum number of minutes required for all fresh oranges to become rotten.
           Returns -1 if it is impossible for all oranges to rot.
      """
      
      # Initialize a queue to keep track of all initially rotten oranges
      q = deque()
      # Initialize time to track the number of minutes passed
      # Initialize fresh to count the number of fresh oranges
      time, fresh = 0, 0
      
      # Get the number of rows and columns in the grid
      ROWS, COLS = len(grid), len(grid[0])
      # Define the possible directions for the spread of rot (right, left, down, up)
      directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
      
      # Populate the queue with the positions of all rotten oranges
      # Count the number of fresh oranges
      for r in range(ROWS):
          for c in range(COLS):
              if grid[r][c] == 1:
                  fresh += 1
              if grid[r][c] == 2:
                  q.append((r, c))

      # Process the grid while there are rotten oranges to spread the rot and fresh oranges left
      while q and fresh > 0:
          # Process all rotten oranges at the current time step
          for i in range(len(q)):
              r, c = q.popleft()
              # Check all four possible directions
              for dr, dc in directions:
                  row, col = dr + r, dc + c
                  # If the neighboring cell is within bounds and contains a fresh orange
                  if (row < 0 or row == ROWS or
                      col < 0 or col == COLS or
                      grid[row][col] != 1):
                      continue
                  # Make the fresh orange rotten
                  grid[row][col] = 2
                  # Add the newly rotten orange to the queue
                  q.append((row, col))
                  # Decrease the count of fresh oranges
                  fresh -= 1
          # Increment the time after processing all current rotten oranges
          time += 1
      
      # If there are no fresh oranges left, return the time taken
      # Otherwise, return -1 indicating not all oranges can rot
      return time if fresh == 0 else -1
  

# Cleaner version of the above code
class Solution2:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        time, fresh = 0, 0

        ROWS, COLS = len(grid), len(grid[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))

        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    row, col = dr + r, dc + c

                    if (min(row, col) < 0 or row == ROWS or col == COLS or
                        grid[row][col] != 1):
                        continue

                    grid[row][col] = 2
                    q.append((row, col))
                    fresh -= 1
            time += 1

        return time if fresh == 0 else -1
    
#Example usage:
if __name__ == '__main__':
    Solution = Solution2()
    grid = [[1,1,0],
            [0,1,1],
            [0,1,2]]
    print(Solution.orangesRotting(grid)) #Expected output: 4
