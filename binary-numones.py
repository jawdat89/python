class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0

        while n:
            # n = n & (n - 1)
            n &= n - 1

            cnt += 1

        # while n:
        #     cnt += n % 2
        #     n = n >> 1

        return cnt
        