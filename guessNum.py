class Solution:
    def guess(self, num: int, secret: int) -> int:
        if num > secret:
            return -1
        elif num < secret:
            return 1
        else:
            return 0


    def guessNumber(self, n: int, secret: int) -> int:
        low, high = 1, n

        while low <= high:
            mid = (low + high) // 2

            check = self.guess(mid, secret)
            if check == 1:
                low = mid + 1
            elif check == -1:
                high = mid - 1
            else:
                return mid
        
        return -1
    

# Example Test Execution
solution = Solution()

# Applying test cases
test_cases = [
    (10, 5),
    (10, 1),
    (10, 10),
    (100, 25),
    (100, 75),
    (1, 1)
]

for n, secret in test_cases:
    result = solution.guessNumber(n, secret)
    print(f"n = {n}, secret = {secret}, result = {result}")
