from typing import List

class Solution:
  def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
      if not obstacleGrid:
          return 0
      M, N = len(obstacleGrid), len(obstacleGrid[0])
      dp = {(M - 1, N - 1): 1 if obstacleGrid[M - 1][N - 1] == 0 else 0}
      
      def dfs(r, c):
          if (r == M or c == N or obstacleGrid[r][c] == 1):
              return 0
          if (r, c) in dp:
              return dp[(r, c)]
          
          dp[(r, c)] = dfs(r + 1, c) + dfs(r, c + 1)
          return dp[(r, c)]

      return dfs(0, 0)

def main():
  solution = Solution()
  
  # Test case 1: Grid with no obstacles
  obstacleGrid1 = [
      [0, 0, 0],
      [0, 0, 0],
      [0, 0, 0]
  ]
  print("Test Case 1:", solution.uniquePathsWithObstacles(obstacleGrid1))  # Expected output: 6

  # Test case 2: Grid with obstacles
  obstacleGrid2 = [
      [0, 0, 0],
      [0, 1, 0],
      [0, 0, 0]
  ]
  print("Test Case 2:", solution.uniquePathsWithObstacles(obstacleGrid2))  # Expected output: 2

  # Test case 3: Grid with obstacles blocking the path
  obstacleGrid3 = [
      [0, 1],
      [0, 0]
  ]
  print("Test Case 3:", solution.uniquePathsWithObstacles(obstacleGrid3))  # Expected output: 1

  # Test case 4: Grid with obstacle at the end
  obstacleGrid4 = [
      [0, 0, 0],
      [0, 0, 0],
      [0, 0, 1]
  ]
  print("Test Case 4:", solution.uniquePathsWithObstacles(obstacleGrid4))  # Expected output: 0

if __name__ == "__main__":
  main()