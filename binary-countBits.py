from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        offset = 1

        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]
        
        return dp

        # res = []
        # i = 0
        # while i != n + 1:
        #     cur = 0
        #     j = i
        #     while j:
        #         j &= j - 1
        #         cur += 1
        #     res.append(cur)
        #     i += 1
        
        # return res

def main():
  # Create an instance of the Solution class
  solution = Solution()
  
  # Test case 1: n = 0
  n = 0
  result = solution.countBits(n)
  print(f"Count of bits from 0 to {n}: {result}")  # Expected output: [0]

  # Test case 2: n = 1
  n = 1
  result = solution.countBits(n)
  print(f"Count of bits from 0 to {n}: {result}")  # Expected output: [0, 1]

  # Test case 3: n = 2
  n = 2
  result = solution.countBits(n)
  print(f"Count of bits from 0 to {n}: {result}")  # Expected output: [0, 1, 1]

  # Test case 4: n = 5
  n = 5
  result = solution.countBits(n)
  print(f"Count of bits from 0 to {n}: {result}")  # Expected output: [0, 1, 1, 2, 1, 2]

  # Test case 5: n = 10
  n = 10
  result = solution.countBits(n)
  print(f"Count of bits from 0 to {n}: {result}")  # Expected output: [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2]

  # Test case 6: n = 15
  n = 15
  result = solution.countBits(n)
  print(f"Count of bits from 0 to {n}: {result}")  # Expected output: [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4]

if __name__ == "__main__":
  main()