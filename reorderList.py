from typing import Optional

# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
      self.val = val
      self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
      if not head or not head.next:
            return

      slow, fast = head, head.next
      while fast and fast.next:
          slow = slow.next
          fast = fast.next.next

      second = slow.next
      prev = slow.next = None
      while second:
          nxt = second.next
          second.next = prev
          prev = second
          second = nxt
      
      first, second = head, prev
      while second:
          tmp1, tmp2 = first.next, second.next
          first.next = second
          second.next = tmp1
          first, second = tmp1, tmp2

# Utility function to create a linked list from a list of values
def create_linked_list(values):
  if not values:
      return None
  head = ListNode(values[0])
  current = head
  for value in values[1:]:
      current.next = ListNode(value)
      current = current.next
  return head

# Utility function to print the linked list
def print_linked_list(head):
  values = []
  current = head
  while current:
      values.append(current.val)
      current = current.next
  print(" -> ".join(map(str, values)))

# Example usage and test cases
if __name__ == '__main__':
  s = Solution()
  
  # Test case 1
  head = create_linked_list([1, 2, 3, 4])
  print("Original list:")
  print_linked_list(head)
  s.reorderList(head)
  print("Reordered list:")
  print_linked_list(head)
  
  # Test case 2
  head = create_linked_list([1, 2, 3, 4, 5])
  print("\nOriginal list:")
  print_linked_list(head)
  s.reorderList(head)
  print("Reordered list:")
  print_linked_list(head)