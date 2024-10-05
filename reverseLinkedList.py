# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # prev = None
        # curr = head

        # while curr:
        #     next_ = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = next_
        
        # return prev
        
        if not head:
            return None

        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head

        head.next = None

        return newHead

# Helper function to create a linked list from a list
def create_linked_list(elements):
    if not elements:
        return None
    head = ListNode(elements[0])
    current = head
    for element in elements[1:]:
        current.next = ListNode(element)
        current = current.next
    return head

# Helper function to print a linked list
def print_linked_list(head):
    elements = []
    current = head
    while current:
        elements.append(current.val)
        current = current.next
    print(elements)

# Test cases
def main():
    solution = Solution()

    # Test case 1: Normal case
    head = create_linked_list([1, 2, 3, 4, 5])
    print("Original list: ")
    print_linked_list(head)
    reversed_head = solution.reverseList(head)
    print("Reversed list: ")
    print_linked_list(reversed_head)
    
    # Test case 2: Single element list
    head = create_linked_list([1])
    print("Original list: ")
    print_linked_list(head)
    reversed_head = solution.reverseList(head)
    print("Reversed list: ")
    print_linked_list(reversed_head)
    
    # Test case 3: Empty list
    head = create_linked_list([])
    print("Original list: ")
    print_linked_list(head)
    reversed_head = solution.reverseList(head)
    print("Reversed list: ")
    print_linked_list(reversed_head)

    # Test case 4: Two elements list
    head = create_linked_list([1, 2])
    print("Original list: ")
    print_linked_list(head)
    reversed_head = solution.reverseList(head)
    print("Reversed list: ")
    print_linked_list(reversed_head)

if __name__ == "__main__":
    main()
