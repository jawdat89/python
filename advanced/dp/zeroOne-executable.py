from typing import List

class Solution:
  def maximumProfit(self, profit: List[int], weight: List[int], capacity: int, method: str = 'dp_1d') -> int:
      """
      Calculate the maximum profit for the knapsack problem using the specified method.
      
      :param profit: List of profits for each item.
      :param weight: List of weights for each item.
      :param capacity: Maximum capacity of the knapsack.
      :param method: Method to use for calculation ('dp_2d', 'dp_1d', 'dfs', 'memo').
      :return: Maximum profit that can be obtained.
      """
      if method == 'dp_2d':
          return self.dp_2d(profit, weight, capacity)
      elif method == 'dp_1d':
          return self.dp_1d(profit, weight, capacity)
      elif method == 'dfs':
          return self.dfsHelper(0, profit, weight, capacity)
      elif method == 'memo':
          N = len(profit)
          cache = [[-1] * (capacity + 1) for _ in range(N)]
          return self.memoHelper(0, profit, weight, capacity, cache)
      else:
          raise ValueError("Invalid method specified. Choose from 'dp_2d', 'dp_1d', 'dfs', 'memo'.")

  def dp_2d(self, profit: List[int], weight: List[int], capacity: int) -> int:
      """
      Dynamic programming approach using a 2D array.
      """
      N, M = len(profit), capacity
      dp = [[0] * (M + 1) for _ in range(N)]

      for i in range(N):
          dp[i][0] = 0

      for c in range(M + 1):
          if weight[0] <= c:
              dp[0][c] = profit[0]

      for i in range(1, N):
          for c in range(1, M + 1):
              skip = dp[i-1][c]
              include = 0
              if c - weight[i] >= 0:
                  include = profit[i] + dp[i - 1][c - weight[i]]
              dp[i][c] = max(include, skip)

      return dp[N-1][M]

  def dp_1d(self, profit: List[int], weight: List[int], capacity: int) -> int:
      """
      Dynamic programming approach using a 1D array.
      """
      N, M = len(profit), capacity
      dp = [0] * (M + 1)

      for c in range(M + 1):
          if weight[0] <= c:
              dp[c] = profit[0]

      for i in range(1, N):
          curRow = [0] * (M + 1)
          for c in range(1, M + 1):
              skip = dp[c]
              include = 0
              if c - weight[i] >= 0:
                  include = profit[i] + dp[c - weight[i]]
              curRow[c] = max(include, skip)
          dp = curRow

      return dp[M]

  def dfsHelper(self, i: int, profit: List[int], weight: List[int], capacity: int) -> int:
      """
      Recursive depth-first search approach.
      """
      if i == len(profit):
          return 0

      # Option 1: Skip the current item
      maxProfit = self.dfsHelper(i + 1, profit, weight, capacity)

      # Option 2: Include the current item (if it fits)
      newCap = capacity - weight[i]
      if newCap >= 0:
          p = profit[i] + self.dfsHelper(i + 1, profit, weight, newCap)
          maxProfit = max(maxProfit, p)

      return maxProfit

  def memoHelper(self, i: int, profit: List[int], weight: List[int], capacity: int, cache: List[List[int]]) -> int:
      """
      Memoized depth-first search approach.
      """
      if i == len(profit):
          return 0
      if cache[i][capacity] != -1:
          return cache[i][capacity]

      # Option 1: Skip the current item
      cache[i][capacity] = self.memoHelper(i + 1, profit, weight, capacity, cache)

      # Option 2: Include the current item (if it fits)
      newCap = capacity - weight[i]
      if newCap >= 0:
          p = profit[i] + self.memoHelper(i + 1, profit, weight, newCap, cache)
          cache[i][capacity] = max(cache[i][capacity], p)

      return cache[i][capacity]

# Example usage:
if __name__ == '__main__':
    solution = Solution()
    
    # Define the profits, weights, and capacity
    profits = [4, 4, 7, 1]
    weights = [5, 2, 3, 1]
    capacity = 8
    
    # Test using the 1D dynamic programming approach
    max_profit_dp_1d = solution.maximumProfit(profits, weights, capacity, method='dp_1d')
    print(f"Maximum Profit using DP 1D: {max_profit_dp_1d}")
    
    # # Test using the 2D dynamic programming approach
    # max_profit_dp_2d = solution.maximumProfit(profits, weights, capacity, method='dp_2d')
    # print(f"Maximum Profit using DP 2D: {max_profit_dp_2d}")
    
    # # Test using the recursive DFS approach
    # max_profit_dfs = solution.maximumProfit(profits, weights, capacity, method='dfs')
    # print(f"Maximum Profit using DFS: {max_profit_dfs}")
    
    # # Test using the memoized DFS approach
    # max_profit_memo = solution.maximumProfit(profits, weights, capacity, method='memo')
    # print(f"Maximum Profit using Memoization: {max_profit_memo}")