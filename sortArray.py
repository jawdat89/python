from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # def quicksort(l, r):
        #     if l >= r:
        #         return
        #     pivot = partition(l, r)
        #     quicksort(l, pivot - 1)
        #     quicksort(pivot + 1, r)

        # def partition(l, r):
        #     pivot = nums[r]
        #     a = l
        #     for i in range(l, r):
        #         if nums[i] < pivot:
        #             nums[a], nums[i] = nums[i], nums[a]
        #             a += 1
        #     nums[a], nums[r] = nums[r], nums[a]
        #     return a

        # quicksort(0, len(nums) - 1)
        # return nums

        def merge(arr, L, M, R):
          left, right = arr[L:M + 1], arr[M + 1:R + 1]
          i, j, k = L, 0, 0 # Initialize pointers for L (j), R (k), and nums (i)

          # Merge the two arrays while there are elements in both
          while j < len(left) and k < len(right):
              if left[j] <= right[k]:
                  arr[i] = left[j]
                  j += 1
              else:
                  arr[i] = right[k]
                  k += 1
              i += 1
          # If there are remaining elements in L, add them to nums
          while j < len(left):
              arr[i] = left[j]
              j += 1
              i += 1

          # If there are remaining elements in R, add them to nums
          while k < len(right):
              arr[i] = right[k]
              k += 1
              i += 1
            

        def mergeSort(arr, l, r):
          if l == r:
              return arr
          m = (l + r) // 2
          mergeSort(arr, l, m)
          mergeSort(arr, m + 1, r)
          merge(arr, l, m, r)
          return arr
        
        def partition(arr, start, end) -> int:
            pivot = arr[end]
            i = start - 1

            for j in range(start, end):
                if arr[j] < pivot:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]

            arr[i + 1], arr[end] = arr[end], arr[i + 1]

            return i + 1
        
        def quickSort(arr, start, end):
            if end <= start:
                return # Base case: if the list is of length 1 or smaller, it's already sorted.
        
            pivot = partition(arr, start, end)

            quickSort(arr, start, pivot - 1)
            quickSort(arr, pivot + 1, end)

            # Call quickSort and then return the sorted nums
        # quickSort(nums, 0, len(nums) - 1)
        # return nums
        return mergeSort(nums, 0, len(nums) - 1)
        
    # def sortArray(self, nums: List[int]) -> List[int]:

    #     # for i in range(1, len(nums)):
    #     #    j = i
    #     #    while j > 0 and nums[j - 1] > nums[j]:
    #     #         nums[j], nums[j - 1] = nums[j - 1], nums[j]
    #     #         j -= 1
            
    #     # return nums   

    #     # def quicksort(l, r):
    #     #     if l >= r:
    #     #         return
    #     #     pivot = partition(l, r)
    #     #     quicksort(l, pivot - 1)
    #     #     quicksort(pivot + 1, r)

    #     # def partition(l, r):
    #     #     pivot = nums[r]
    #     #     a = l
    #     #     for i in range(l, r):
    #     #         if nums[i] < pivot:
    #     #             nums[a], nums[i] = nums[i], nums[a]
    #     #             a += 1
    #     #     nums[a], nums[r] = nums[r], nums[a]
    #     #     return a

    #     # quicksort(0, len(nums) - 1)
    #     # return nums

    #     # Base case: if the list is of length 1 or smaller, it's already sorted.
    #     if len(nums) > 1:
    #         # Find the middle index to divide the array into two halves
    #         mid = len(nums) // 2
    #         # Divide the array into two halves, L and R
    #         L = nums[:mid]
    #         R = nums[mid:]

    #         # Recursively sort both halves
    #         self.sortArray(L)
    #         self.sortArray(R)

    #         # Merge the sorted halves
    #         i = j = k = 0  # Initialize pointers for L (i), R (j), and nums (k)

    #         # Merge the two arrays while there are elements in both
    #         while i < len(L) and j < len(R):
    #             if L[i] < R[j]:
    #                 nums[k] = L[i]
    #                 i += 1
    #             else:
    #                 nums[k] = R[j]
    #                 j += 1
    #             k += 1

    #         # If there are remaining elements in L, add them to nums
    #         while i < len(L):
    #             nums[k] = L[i]
    #             i += 1
    #             k += 1

    #         # If there are remaining elements in R, add them to nums
    #         while j < len(R):
    #             nums[k] = R[j]
    #             j += 1
    #             k += 1

    #     # Return the sorted array
    #     return nums

        
        
            
            

       
            

if __name__ == "__main__":
    solution = Solution()
    print(solution.sortArray([2,1,3]))  # Expected output: 2
    print(solution.sortArray([4,1,3,2]))  # Expected output: 3
    print(solution.sortArray([3,1,5,2,4]))  # Expected output: 8
