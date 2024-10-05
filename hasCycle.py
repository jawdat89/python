# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        # nodeSet = set()

        # cur = head
        # while cur:
        #     if cur in nodeSet:
        #         return True
        #     nodeSet.add(cur)
        #     cur = cur.next
        # return False
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False