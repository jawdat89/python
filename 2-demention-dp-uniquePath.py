class Solution:
  def uniquePaths(self, m: int, n: int) -> int:
    #   # Initialize the previous row with zeros
    #   prevRow = [0] * n

    #   # Iterate from the last row to the first row
    #   for r in range(m - 1, -1, -1):
    #       # Initialize the current row with zeros
    #       curRow = [0] * n
    #       # Set the last column of the current row to 1
    #       curRow[n - 1] = 1
    #       # Iterate from the second last column to the first column
    #       for c in range(n - 2, -1, -1):
    #           # Calculate the number of unique paths to the right and below
    #           curRow[c] = curRow[c + 1] + prevRow[c]
    #       # Update the previous row to be the current row
    #       prevRow = curRow

    #   # Return the number of unique paths from the top-left corner
    #   return prevRow[0]
        dp = [0] * n
        dp[n - 1] = 1

        for r in reversed(range(m)):
            for c in reversed(range(n)):
                if c + 1 < n:
                    dp[c] = dp[c] + dp[c + 1]
        return dp[0]

def main():
  # Create an instance of the Solution class
  solution = Solution()
  
  # Test case 1: 3x7 grid
  m, n = 3, 7
  result = solution.uniquePaths(m, n)
  print(f"Number of unique paths in a {m}x{n} grid: {result}")  # Expected output: 28

  # Test case 2: 3x2 grid
  m, n = 3, 2
  result = solution.uniquePaths(m, n)
  print(f"Number of unique paths in a {m}x{n} grid: {result}")  # Expected output: 3

  # Test case 3: 7x3 grid
  m, n = 7, 3
  result = solution.uniquePaths(m, n)
  print(f"Number of unique paths in a {m}x{n} grid: {result}")  # Expected output: 28

if __name__ == "__main__":
  main()