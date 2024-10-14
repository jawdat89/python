class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L, R = 0, len(numbers) - 1

        while L < R:
            res = numbers[L] + numbers[R]

            if res > target:
                R -= 1
            elif res < target:
                L += 1
            else:
                return [L + 1, R + 1]

        return []