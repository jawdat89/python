from typing import List

class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value

class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        # res = []
        # # Initially, append a copy of the original list to res
        # res.append(list(pairs))

        # # Start from the second element as the first element is already "sorted"
        # for i in range(1, len(pairs)):
        #     current = pairs[i]
        #     j = i - 1

        #     # Move elements of pairs[0..i-1], that are greater than current.key, to one position ahead of their current position
        #     while j >= 0 and current.key < pairs[j].key:
        #         pairs[j + 1] = pairs[j]
        #         j -= 1
            
        #     pairs[j + 1] = current

        #     # Append a copy of the current state of pairs to res
        #     res.append(list(pairs))
        

        n = len(pairs)
        res = [] # Intermediate states of the list of pairs

        # Loop through the list of pairs
        for i in range(n):
            j = i - 1

            while j >= 0 and pairs[j].key > pairs[j + 1].key:
                pairs[j], pairs[j + 1] = pairs[j + 1], pairs[j]
                j -= 1
            # Clone and save the entire state of the array at this point
            res.append(pairs[:])

        return res


# Test Case 1
pairs1 = [Pair(5, "apple"), Pair(2, "banana"), Pair(9, "cherry")]
solution = Solution()
sorted_pairs1 = solution.insertionSort(pairs1)
print("Test Case 1 Results:")
for state in sorted_pairs1:
    print([(pair.key, pair.value) for pair in state])

# Test Case 2
pairs2 = [Pair(3, "cat"), Pair(3, "bird"), Pair(2, "dog")]
sorted_pairs2 = solution.insertionSort(pairs2)
print("\nTest Case 2 Results:")
for state in sorted_pairs2:
    print([(pair.key, pair.value) for pair in state])

# Test Case 3
pairs3 = [Pair(1, "orange"), Pair(0, "grape"), Pair(4, "mango"), Pair(2, "kiwi")]
sorted_pairs3 = solution.insertionSort(pairs3)
print("\nTest Case 3 Results:")
for state in sorted_pairs3:
    print([(pair.key, pair.value) for pair in state])