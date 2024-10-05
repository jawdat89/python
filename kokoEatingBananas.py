import math
from typing import List

class Solution:
  # def minEatinSpeed(self, piles: List[int], h: int) -> int:
  #   # Binary search
  #   # Declare low and high
  #   low, high = 1, max(piles)

  #   # koko eating speed is in between 1 and max(piles)
  #   # time is the total time taken to eat all bananas
  #   # if time > h, then increase the speed; meaning that koko is eating too slow vs max piles per hour
  #   # if time <= h, then decrease the speed; meaning that koko is eating too fast vs max piles per hour

  #   # while koko eating speed is in between low and high; meaning that koko is eating 
  #   # at a speed that is not too slow or too fast
  #   while low <= high:
  #     mid = (low + high) // 2

  #     time = 0
  #     for pile in piles:
  #       time += (pile + mid - 1) // mid

  #     if time > h:
  #       low = mid + 1
  #     else:
  #       high = mid - 1

  #   # return the value of piles per hour that koko can eat
  #   return low
  def minEatinSpeed(self, piles: List[int], h: int) -> int:
    # Initialize the left and right pointers for binary search
    l, r = 1, max(piles)

    # Variable to store the result of the minimum eating speed
    res = r

    # Perform binary search
    while l <= r:
      # Calculate the mid point
      k = (l + r) // 2

      # Calculate the total hours to eat all bananas
      hours = 0
      for p in piles:
        # Calculate the number of hours needed for each pile and sum them up
        hours += math.ceil(p / k)  

      # If the total hours needed is less than or equal to `h`, 
      # update the result and move the right pointer to search for a smaller speed
      if hours <= h:
        res = min(res, k)
        r = k - 1
      # If the total hours needed is more than `h`, move the left pointer to search for a larger speed
      else:
        l = k + 1

    # Return the result
    return res


  
# Example Test Execution
solution = Solution()

# Applying test cases
test_cases = [
  ([3, 6, 7, 11], 8),
  ([30, 11, 23, 4, 20], 5),
  ([30, 11, 23, 4, 20], 6)
]

for piles, h in test_cases:
  result = solution.minEatinSpeed(piles, h)
  print(f"piles = {piles}, h = {h}, result = {result}")

# Output:
# piles = [3, 6, 7, 11], h = 8, result = 4
# piles = [30, 11, 23, 4, 20], h = 5, result = 30
# piles = [30, 11, 23, 4, 20], h = 6, result = 23
