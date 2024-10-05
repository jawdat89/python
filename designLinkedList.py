class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.prev = None
        self.next = None

class MyLinkedList:
        
    def __init__(self):
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, index: int) -> int:
        cur = self.head.next
        while cur != self.tail and index > 0:
            cur = cur.next
            index -= 1
        
        if cur != self.tail and index == 0:
            return cur.val
        return -1
            
    def addAtHead(self, val: int) -> None:
        node, next, prev = ListNode(val), self.head.next, self.head
        node.next = next
        node.prev = prev
        next.prev = node
        prev.next = node

    def addAtTail(self, val: int) -> None:
        node, next, prev = ListNode(val), self.tail, self.tail.prev
        node.next = next
        node.prev = prev
        next.prev = node
        prev.next = node
        
    def addAtIndex(self, index: int, val: int) -> None:
        cur = self.head.next
        while cur != self.tail and index > 0:
            cur = cur.next
            index -= 1
        
        if cur and index == 0:
            node, next, prev = ListNode(val), cur, cur.prev
            node.next = next
            node.prev = prev
            next.prev = node
            prev.next = node

    def deleteAtIndex(self, index: int) -> None:
        cur = self.head.next
        while cur != self.tail and index > 0:
            cur = cur.next
            index -= 1
        
        if cur != self.tail and index == 0:
            next, prev = cur.next, cur.prev
            next.prev = prev
            prev.next = next

def print_linked_list(linked_list):
    current = linked_list.head.next
    result = []
    while current != linked_list.tail:
        result.append(current.val)
        current = current.next
    print(result)

def main():
    linked_list = MyLinkedList()
    
    # Test addAtHead
    linked_list.addAtHead(1)
    print("After addAtHead(1):", end=" ")
    print_linked_list(linked_list)
    
    linked_list.addAtHead(2)
    print("After addAtHead(2):", end=" ")
    print_linked_list(linked_list)
    
    # Test addAtTail
    linked_list.addAtTail(3)
    print("After addAtTail(3):", end=" ")
    print_linked_list(linked_list)
    
    linked_list.addAtTail(4)
    print("After addAtTail(4):", end=" ")
    print_linked_list(linked_list)
    
    # Test addAtIndex
    linked_list.addAtIndex(2, 5)
    print("After addAtIndex(2, 5):", end=" ")
    print_linked_list(linked_list)
    
    # Test get
    print("Get element at index 2:", linked_list.get(2))  # Should return 5
    print("Get element at index 4:", linked_list.get(4))  # Should return 3
    print("Get element at index 5:", linked_list.get(5))  # Should return -1 (out of range)
    
    # Test deleteAtIndex
    linked_list.deleteAtIndex(2)
    print("After deleteAtIndex(2):", end=" ")
    print_linked_list(linked_list)
    
    linked_list.deleteAtIndex(0)
    print("After deleteAtIndex(0):", end=" ")
    print_linked_list(linked_list)

if __name__ == "__main__":
    main()
