# Time: O(n^2 * n!)
def permutationsRecursive(nums):
    return helper(0, nums)
        
def helper(i, nums):   
    if i == len(nums):
        return [[]]
    
    resPerms = []
    perms = helper(i + 1, nums)
    for p in perms:
        for j in range(len(p) + 1):
            pCopy = p.copy()
            pCopy.insert(j, nums[i])
            resPerms.append(pCopy)
    return resPerms

# Example: [1, 2, 3]
# perms = [
#           [1, 2, 3], 
#           [2, 1, 3],
#           [2, 3, 1], 
#           [1, 3, 2], 
#           [3, 1, 2], 
#           [3, 2, 1]
#         ]

# Time: O(n^2 * n!)
def permutationsIterative(nums):
    perms = [[]]

    for n in nums:
        nextPerms = []
        for p in perms:
            for i in range(len(p) + 1):
                pCopy = p.copy()
                pCopy.insert(i, n)
                nextPerms.append(pCopy)
        perms = nextPerms
    return perms

# Example: [1, 2, 3]
# perms = [
#           [1, 2, 3],
#           [1, 3, 2],
#           [2, 1, 3],
#           [2, 3, 1],
#           [3, 1, 2],
#           [3, 2, 1]
#         ]