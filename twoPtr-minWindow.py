from typing import List

class Solution:
  def minWindow(self, s: str, t: str) -> str:
      # If t is empty, return an empty string as there's nothing to find
      if t == "":
          return ""

      # Dictionaries to count characters in t and the current window in s
      countT, window = {}, {}

      # Count the frequency of each character in t
      for c in t:
          countT[c] = 1 + countT.get(c, 0)

      # Initialize variables to track the number of characters we need and have
      have, need = 0, len(countT)

      # Result variables to store the best window found
      res, resLen = [-1, -1], float('inf')
      L = 0  # Left pointer of the window

      # Iterate over each character in s with the right pointer R
      for R in range(len(s)):
          c = s[R]  # Current character at the right pointer

          # Add the current character to the window count
          window[c] = 1 + window.get(c, 0)

          # If the current character is needed and its count matches the required count
          if c in countT and window[c] == countT[c]:
              have += 1

          # While the window is valid (contains all characters of t with required frequency)
          while have == need:
              # Update the result if the current window is smaller than the previously found window
              if (R - L + 1) < resLen:
                  res = [L, R]
                  resLen = (R - L + 1)

              # Pop the leftmost character from the window
              window[s[L]] -= 1
              # If the popped character is needed and its count is now less than required, update 'have'
              if s[L] in countT and window[s[L]] < countT[s[L]]:
                  have -= 1
              # Move the left pointer to the right to try and find a smaller window
              L += 1

      # Extract the result window from s using the indices stored in res
      l, r = res
      return s[l:r + 1] if resLen != float('inf') else ""