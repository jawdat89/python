class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]

        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])

        return dp[0][0]

def main():
    # Create an instance of the Solution class
    solution = Solution()
    
    # Test case 1: Both strings are empty
    text1, text2 = "", ""
    result = solution.longestCommonSubsequence(text1, text2)
    print(f"LCS of '{text1}' and '{text2}': {result}")  # Expected output: 0

    # Test case 2: Identical strings
    text1, text2 = "abc", "abc"
    result = solution.longestCommonSubsequence(text1, text2)
    print(f"LCS of '{text1}' and '{text2}': {result}")  # Expected output: 3

    # Test case 3: No common subsequence
    text1, text2 = "abc", "def"
    result = solution.longestCommonSubsequence(text1, text2)
    print(f"LCS of '{text1}' and '{text2}': {result}")  # Expected output: 0

    # Test case 4: Partial overlap
    text1, text2 = "abc", "ac"
    result = solution.longestCommonSubsequence(text1, text2)
    print(f"LCS of '{text1}' and '{text2}': {result}")  # Expected output: 2

    # Test case 5: Interleaved subsequence
    text1, text2 = "abcde", "ace"
    result = solution.longestCommonSubsequence(text1, text2)
    print(f"LCS of '{text1}' and '{text2}': {result}")  # Expected output: 3

    # Test case 6: Complex case
    text1, text2 = "abcbdab", "bdcaba"
    result = solution.longestCommonSubsequence(text1, text2)
    print(f"LCS of '{text1}' and '{text2}': {result}")  # Expected output: 4

if __name__ == "__main__":
    main()