class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1  # Base cases: one for step 1, two for step 0 (ground)
        
        for i in range(n-1):  # Loop runs n-1 times
            temp = one
            one = one + two  # Update one to the sum of one and two (ways to reach current step)
            two = temp  # Update two to the old value of one (ways to reach the previous step)

        return one  # The result is stored in one
  
    # dynamic programming
    def climbStairsDynamic(self,n: int) -> int:
        if n <= 1:
            return 1

        dp = [0] * (n + 1)  # Create an array of length n+1, initialized to 0
        dp[0] = 1  # Base case: 1 way to stay at the ground (0-th step)
        dp[1] = 1  # Base case: 1 way to reach the first step

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]  # Number of ways to reach the i-th step

        return dp[n]  # Return the number of ways to reach the n-th step


if __name__ == "__main__":
    solution = Solution()
    print(solution.climbStairsDynamic(2))  # Expected output: 2
    print(solution.climbStairsDynamic(3))  # Expected output: 3
    print(solution.climbStairsDynamic(4))  # Expected output: 5
    print(solution.climbStairsDynamic(5))  # Expected output: 8


class Solution2:
    def factorial(self, n: int) -> int:
        if n == 0:
            return 1
        
        dp = [0] * (n + 1)

        dp[0] = 1
        dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = i * dp[i - 1]

        return dp[n]
    
    def factorialItterative(self, n: int) -> int:
        res = 1  

        for i in range(2, n+1):  
            res *= i  

        return res  # The result is stored in one
    
    def factorialRecursive(self, n: int) -> int:
        if n <= 1:
            return 1
        
        return n * self.factorialRecursive(n - 1)