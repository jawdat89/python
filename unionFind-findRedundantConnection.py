from typing import List

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # Find the maximum node number to size the parent and rank arrays correctly
        max_node = max(max(u, v) for u, v in edges)
        par = [i for i in range(max_node + 1)]
        rank = [1] * (max_node + 1)

        # Find function with path compression
        def find(n):
            p = par[n]
            while p != par[p]:
                par[p] = par[par[p]]  # Path compression
                p = par[p]
            return p

        # Union function with union by rank
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            # If both nodes have the same parent, the edge is redundant
            if p1 == p2:
                return False

            # Union by rank
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]

            return True

        # Iterate over each edge and apply union-find
        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]

        return []

# Test cases for debugging
def test_redundant_connection():
    solution = Solution()

    # Test case 1: Simple cycle
    edges1 = [[1, 2], [1, 3], [2, 3]]
    result1 = solution.findRedundantConnection(edges1)
    print(f"Test case 1 result: {result1}\n")  # Expected: [2, 3]

    # Test case 2: Larger cycle
    edges2 = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]
    result2 = solution.findRedundantConnection(edges2)
    print(f"Test case 2 result: {result2}\n")  # Expected: [1, 4]

    # Test case 3: No redundant connection (not possible per problem constraints)
    # This test case is invalid for the problem constraints, but let's handle it gracefully
    edges3 = [[1, 2], [2, 3], [3, 4]]
    try:
        result3 = solution.findRedundantConnection(edges3)
        print(f"Test case 3 result: {result3}\n")  # Expected: []
    except IndexError as e:
        print(f"Test case 3 encountered an error: {e}\n")

if __name__ == "__main__":
    test_redundant_connection()