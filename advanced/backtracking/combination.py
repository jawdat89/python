# Given n numbers (1 - n), return all possible combinations
# of size k. (n choose k math problem).
# Time: O(k * 2^n)
def combinations(n, k):
    combs = []
    helper(1, [], combs, n, k)
    return combs

def helper(i, curComb, combs, n, k):
    if len(curComb) == k:
        combs.append(curComb.copy())
        return
    if i > n:
        return
    
    # decision to include i
    curComb.append(i)
    helper(i + 1, curComb, combs, n, k)
    curComb.pop()
    
    # decision to NOT include i
    helper(i + 1, curComb, combs, n, k)


# Time: O(k * C(n, k))
# formula: C(n, k) = C(n - 1, k - 1) + C(n - 1, k)
# math: C(n, k) = n! 
#       /
#       (k! * (n - k)!)
def combinations2(n, k):
    combs = []
    helper2(1, [], combs, n, k)
    return combs

def helper2(i, curComb, combs, n, k):
    if len(curComb) == k:
        combs.append(curComb.copy())
        return
    if i > n:
        return
    
    for j in range(i, n + 1):
        curComb.append(j)
        helper2(j + 1, curComb, combs, n, k)
        curComb.pop()


# Dynamic Programming approach
def combinations2(n, k):
    combs = []
    helper3(n, k, combs)
    return combs

def helper3(n, k, combs):
    # Initialize a list to store combinations of different sizes
    dp = [[] for _ in range(k + 1)]
    dp[0] = [[]]  # Base case: one way to choose 0 elements

    # Iterate over each number from 1 to n
    for num in range(1, n + 1):
        # Update combinations in reverse order to avoid overwriting
        for j in range(min(k, num), 0, -1):
            # Add current number to each combination of size j-1
            for comb in dp[j - 1]:
                dp[j].append(comb + [num])

    return dp[k]