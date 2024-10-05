
from typing import List

# Definition for a pair.
class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value
class Solution:
    # def partition(self, arr, start, end) -> int:
    #     pivot = arr[end].key
    #     i = start - 1

    #     for j in range(start, end):
    #         if arr[j].key < pivot:
    #             i += 1
    #             arr[i], arr[j] = arr[j], arr[i]
        
    #     arr[i + 1], arr[end] = arr[end], arr[i + 1]

    #     return i + 1

    # def sortPairs(self, arr, start, end):
    #     if end <= start:
    #         return arr
        
    #     pivot = self.partition(arr, start, end)

    #     self.sortPairs(arr, start, pivot - 1)
    #     self.sortPairs(arr, pivot + 1, end)
    
    # def quickSort(self, pairs: List[Pair]) -> List[Pair]:
    #     n = len(pairs)
    #     self.sortPairs(pairs, 0, n - 1)

    #     return pairs

    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self.quickSortHelper(pairs, 0, len(pairs) - 1)
        return pairs
        
    def quickSortHelper(self, pairs, s, e):
      if e - s + 1 <= 1:
          return

      pivot = pairs[e] # Right most
      left = s


      for i in range(s, e):
          # partition
          if pairs[i].key < pivot.key:
              tmp = pairs[left]
              pairs[left] = pairs[i]
              pairs[i] = tmp
              left += 1
      # Move pivor in-between left and right sides
      pairs[e] = pairs[left]
      pairs[left] = pivot

      
      self.quickSortHelper(pairs, s, left - 1) # left
      self.quickSortHelper(pairs, left + 1, e) # right

            

        


    
# Test Case 1
pairs = [Pair(3, "cat"), Pair(2, "dog"), Pair(3, "bird")]
solution = Solution()
sorted_pairs = solution.quickSort(pairs)
print([(pair.key, pair.value) for pair in sorted_pairs])
# Expected Output: [(2, "dog"), (3, "bird"), (3, "cat")]
# Test Case 2
pairs = [Pair(5, "apple"), Pair(9, "banana"), Pair(9, "cherry"), Pair(1, "date"), Pair(9, "elderberry")]
solution = Solution()
sorted_pairs = solution.quickSort(pairs)
print([(pair.key, pair.value) for pair in sorted_pairs])
# Expected Output: [(1, "date"), (5, "apple"), (9, "banana"), (9, "cherry"), (9, "elderberry")]
# Test Case 3
pairs = [Pair(10, "zebra"), Pair(1, "aardvark"), Pair(7, "kangaroo"), Pair(3, "elephant")]
solution = Solution()
sorted_pairs = solution.quickSort(pairs)
print([(pair.key, pair.value) for pair in sorted_pairs])
# Expected Output: [(1, "aardvark"), (3, "elephant"), (7, "kangaroo"), (10, "zebra")]
# Test Case 4
pairs = []
solution = Solution()
sorted_pairs = solution.quickSort(pairs)
print([(pair.key, pair.value) for pair in sorted_pairs])
# Expected Output: []
# Test Case 5
pairs = [Pair(2, "banana"), Pair(1, "apple"), Pair(4, "date"), Pair(3, "cherry"), Pair(5, "elderberry")]
solution = Solution()
sorted_pairs = solution.quickSort(pairs)
print([(pair.key, pair.value) for pair in sorted_pairs])
# Expected Output: [(1, "apple"), (2, "banana"), (3, "cherry"), (4, "date"), (5, "elderberry")]
