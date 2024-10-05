import heapq
from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        """
        Initialize the min heap data structure with the given integers.

        :param k: The number of largest integers to store in the min heap.
        :param nums: The list of initial integers to add to the min heap.
        """
        # Initialize a minHeap with K largest integers
        self.minHeap, self.k = nums, k
        
        # Heapify the minHeap to maintain a valid heap structure
        heapq.heapify(self.minHeap)
        
        # Remove excess elements from the minHeap to ensure it contains only K largest integers
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        """
        Add a new integer to the min heap and return the Kth largest integer.

        :param val: The new integer to add to the min heap.
        :return: The Kth largest integer currently in the min heap.
        """
        # Push the new value onto the minHeap
        heapq.heappush(self.minHeap, val)
        
        # If the minHeap has more than K elements, remove the smallest one (bottom of the heap)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

        # Return the Kth largest integer currently in the minHeap (the minimum element)
        return self.minHeap[0]


if __name__ == "__main__":
    k = 3
    nums = [4,5,8,2]
    obj = KthLargest(k,nums)
    
    print(obj.add(3)) # returns 4 
    print(obj.add(5)) # returns 5 
    print(obj.add(10))# returns 5 
    print(obj.add(1))  # returns 5
    print(obj.add(20)) # returns 8 
    print(obj.add(-99)) # returns 8
