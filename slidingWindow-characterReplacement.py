class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L = 0
        maxF = 0 # max Frequent character

        count = {}

        for R in range(len(s)):
            count[s[R]] = 1 + count.get(s[R], 0)
            maxF = max(maxF, count[s[R]])

            # if (R - L + 1) - max(count.values()) > k: <-- less efficiant

            # while (R - L + 1) - maxF > k: 
            if (R - L + 1) - maxF > k:
                count[s[L]] -= 1
                L += 1

        return (R - L + 1)