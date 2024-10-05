from typing import List
import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        negated_stones = [-stone for stone in stones]

        heapq.heapify(negated_stones)

        while len(negated_stones) > 1:
            first = -heapq.heappop(negated_stones)
            second = -heapq.heappop(negated_stones)

            res = first - second
            
            if res > 0:
                heapq.heappush(negated_stones, -res)

        return abs(negated_stones[0]) if negated_stones else 0