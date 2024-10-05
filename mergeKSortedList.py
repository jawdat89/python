### You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

# Merge all the linked-lists into one sorted linked-list and return it.

 

# Example 1:

# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# merging them into one sorted list:
# 1->1->2->3->4->4->5->6
# Example 2:

# Input: lists = []
# Output: []
# Example 3:

# Input: lists = [[]]
# Output: []
 

# Constraints:

# k == lists.length
# 0 <= k <= 104
# 0 <= lists[i].length <= 500
# -104 <= lists[i][j] <= 104
# lists[i] is sorted in ascending order.
# The sum of lists[i].length will not exceed 104.

from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeList(self, l1, l2):
            dummy = ListNode()
            tail = dummy

            while l1 and l2:
                if l1.val < l2.val:
                    tail.next = l1
                    l1 = l1.next
                else:
                    tail.next = l2
                    l2 = l2.next
                tail = tail.next
            
            if l1:
                tail.next = l1
            elif l2:
                tail.next = l2
            
            return dummy.next
            
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0: # edge cases
            return None
        
        while len(lists) > 1:
            mergedLists = []
            
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                mergedLists.append(self.mergeList(l1, l2))
            lists = mergedLists
        return lists[0]

# Helper functions
def build_linked_lists(lists):
    linked_lists = []
    for sublist in lists:
        dummy = ListNode()
        current = dummy
        for value in sublist:
            current.next = ListNode(value)
            current = current.next
        linked_lists.append(dummy.next)
    return linked_lists

def linked_list_to_array(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

# Test cases
solution = Solution()

# Example 1
lists1 = build_linked_lists([[1,4,5],[1,3,4],[2,6]])
merged1 = solution.mergeKLists(lists1)
print("Example 1 Output:", linked_list_to_array(merged1))

# Example 2
lists2 = build_linked_lists([])
merged2 = solution.mergeKLists(lists2)
print("Example 2 Output:", linked_list_to_array(merged2) if merged2 else [])

# Example 3
lists3 = build_linked_lists([[]])
merged3 = solution.mergeKLists(lists3)
print("Example 3 Output:", linked_list_to_array(merged3) if merged3 else [])