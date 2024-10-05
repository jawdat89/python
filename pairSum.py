# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        if not head or not head.next:
            return 0

        slow, fast = head, head
        prev = None
        while fast and fast.next:
            fast = fast.next.next

            slowNxt = slow.next
            slow.next = prev
            prev = slow
            slow = slowNxt

        res = 0

        first, second = prev, slow
        while second:
            res = max(res, first.val + second.val)
            first, second = first.next, second.next

        return res

# call the function
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

def print_linked_list(head):
    values = []
    current = head
    while current:
        values.append(current.val)
        current = current.next
    print(" -> ".join(map(str, values)))

if __name__ == '__main__':
    s = Solution()
    head = create_linked_list([5, 4, 2, 1])
    print("Original list:")
    print_linked_list(head)
    print("Max sum of pairs:")
    print(s.pairSum(head))

    head = create_linked_list([4, 2, 2, 3])
    print("\nOriginal list:")
    print_linked_list(head)
    print("Max sum of pairs:")
    print(s.pairSum(head))

    head = create_linked_list([1, 10001])
    print("\nOriginal list:")
    print_linked_list(head)
    print("Max sum of pairs:")
    print(s.pairSum(head))