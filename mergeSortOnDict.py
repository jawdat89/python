from typing import List

class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value

class Solution:
    # def merge(self, pairs: List[Pair], L, M, R):
    #       left, right = pairs[L:M + 1], pairs[M + 1:R + 1]
    #       i, j, k = L, 0, 0 # Initialize pointers for L (j), R (k), and nums (i)

    #       # Merge the two arrays while there are elements in both
    #       while j < len(left) and k < len(right):
    #           if left[j].key <= right[k].key:
    #               pairs[i] = left[j]
    #               j += 1
    #           else:
    #               pairs[i] = right[k]
    #               k += 1
    #           i += 1
    #       # If there are remaining elements in L, add them to nums
    #       while j < len(left):
    #           pairs[i] = left[j]
    #           j += 1
    #           i += 1

    #       # If there are remaining elements in R, add them to nums
    #       while k < len(right):code
    #           pairs[i] = right[k]
    #           k += 1
    #           i += 1


    # def mergeListSort(self, pairs: List[Pair],l, r):
    #     n = len(pairs)
    #     if l == r:
    #         return pairs

    #     md = (l + r) // 2
    #     self.mergeListSort(pairs, l, md)
    #     self.mergeListSort(pairs, md + 1, r)
    #     self.merge(pairs, l, md, r)

    #     return pairs


    
    # def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        # self.mergeListSort(pairs, 0, len(pairs) - 1)
        # return pairs
    
    def merge(self, arr, s, m, e): 
        L = arr[s: m + 1]
        R = arr[m + 1: e + 1]

        i = 0 # index L
        j = 0 # index R
        k = s # index arr

        # Merge the two sorted halfs
        while i < len(L) and j < len(R):
            if L[i].key <= R[j].key:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Add the remaining elements in L to arr
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        
        # Add the remaining elements in R to arr
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    
    def mergeSortHelper(self, pairs, s, e):
        if e - s + 1 <= 1:
            return pairs
        

        m = (s + e) // 2 # s + (e - s) // 2

        self.mergeSortHelper(pairs, s, m)
        self.mergeSortHelper(pairs, m + 1, e)

        self.merge(pairs, s, m, e)

        return pairs

    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.mergeSortHelper(pairs, 0, len(pairs) - 1)



# Test Case 1
pairs1 = [Pair(5, "apple"), Pair(2, "banana"), Pair(9, "cherry")]
solution = Solution()
solution.mergeSort(pairs1)
print("Test Case 1 Results:")
for pair in pairs1:
    print((pair.key, pair.value))

# Test Case 2
pairs2 = [Pair(3, "cat"), Pair(3, "bird"), Pair(2, "dog")]
solution.mergeSort(pairs2)
print("\nTest Case 2 Results:")
for pair in pairs2:
    print((pair.key, pair.value))

# Test Case 3
pairs3 = [Pair(1, "orange"), Pair(0, "grape"), Pair(4, "mango"), Pair(2, "kiwi")]
solution.mergeSort(pairs3)
print("\nTest Case 3 Results:")
for pair in pairs3:
    print((pair.key, pair.value))