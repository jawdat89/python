class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        L, R = 0, 1
        maxSize, prev = 1, ""

        while R < len(arr):
            if arr[R - 1] > arr[R] and prev != '>':
                maxSize = max(maxSize, R - L + 1)
                R += 1
                prev = '>'
            elif arr[R - 1] < arr[R] and prev != '<':
                maxSize = max(maxSize, R - L + 1)
                R += 1
                prev = '<'
            else:
                R = R + 1 if arr[R] == arr[R - 1] else R 
                L = R - 1
                prev = ''


        return maxSize
