class Solution:
  def reverseBits(self, n: int) -> int:
      res = 0
      for i in range(32):
          bit = (n >> i) & 1
          res = res | (bit << (31 - i))
      return res

def main():
  # Create an instance of the Solution class
  solution = Solution()
  
  # Test case 1: n = 0 (all bits are zero)
  n = 0
  result = solution.reverseBits(n)
  print(f"Reversed bits of {n}: {result} (binary: {result:032b})")  # Expected output: 0

  # Test case 2: n = 1 (only the least significant bit is set)
  n = 1
  result = solution.reverseBits(n)
  print(f"Reversed bits of {n}: {result} (binary: {result:032b})")  # Expected output: 2147483648 (binary: 10000000000000000000000000000000)

  # Test case 3: n = 2 (second least significant bit is set)
  n = 2
  result = solution.reverseBits(n)
  print(f"Reversed bits of {n}: {result} (binary: {result:032b})")  # Expected output: 1073741824 (binary: 01000000000000000000000000000000)

  # Test case 4: n = 4294967295 (all bits are set)
  n = 4294967295
  result = solution.reverseBits(n)
  print(f"Reversed bits of {n}: {result} (binary: {result:032b})")  # Expected output: 4294967295 (binary: 11111111111111111111111111111111)

  # Test case 5: n = 43261596 (random bit pattern)
  n = 43261596
  result = solution.reverseBits(n)
  print(f"Reversed bits of {n}: {result} (binary: {result:032b})")  # Expected output: 964176192 (binary: 00111001011110000010100101000000)

if __name__ == "__main__":
  main()