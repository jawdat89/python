class ListNode:
    def __init__(self, val=None):
        self.val = val
        self.next = None
        self.prev = None

# class BrowserHistory:

#     def __init__(self, homepage: str):
#         self.current = ListNode(homepage)
#         self.head = ListNode
#         self.tail = ListNode
#         self.head.next = self.current
#         self.tail.prev = self.current
#         self.current.prev = self.head
#         self.current.next = self.tail
        

#     def visit(self, url: str) -> None:
#         node, next, prev = ListNode(url), self.tail, self.current
#         node.next = next
#         node.prev = prev
#         next.prev = node
#         prev.next = node
#         self.current = node

#     def back(self, steps: int) -> str:
#         while steps > 0 and self.current.prev != self.head:
#             self.current = self.current.prev
#             steps -= 1
#         return self.current.val
        

#     def forward(self, steps: int) -> str:
#         while steps > 0 and self.current.next != self.tail:
#             self.current = self.current.next
#             steps -= 1
#         return self.current.val

# using stack
class BrowserHistory:
    def __init__(self, homepage: str):
        self.history = [homepage]
        self.cur = 0

    def visit(self, url: str) -> None:
        # check if there is forward history
        self.cur += 1
        if self.cur < len(self.history):
            self.history[self.cur] = url    # Overwrite
            self.history = self.history[:self.cur + 1]
        else:
            self.history.append(url)        # Add

    def back(self, steps: int) -> str:
        self.cur = max(0, self.cur - steps)
        return self.history[self.cur]

    def forward(self, steps: int) -> str:
        self.cur = min(len(self.history) - 1, self.cur + steps)
        return self.history[self.cur]
  

def main():
    # Test case 1
    browserHistory = BrowserHistory("leetcode.com")
    browserHistory.visit("google.com")
    browserHistory.visit("facebook.com")
    browserHistory.visit("youtube.com")
    print(browserHistory.back(1))  # Should return "facebook.com"
    print(browserHistory.back(1))  # Should return "google.com"
    print(browserHistory.forward(1))  # Should return "facebook.com"
    browserHistory.visit("linkedin.com")
    print(browserHistory.forward(2))  # Should return "linkedin.com"
    print(browserHistory.back(2))  # Should return "google.com"
    print(browserHistory.back(7))  # Should return "leetcode.com"

    # Additional test case 2
    browserHistory = BrowserHistory("startpage.com")
    browserHistory.visit("page1.com")
    browserHistory.visit("page2.com")
    print(browserHistory.back(1))  # Should return "page1.com"
    browserHistory.visit("page3.com")
    print(browserHistory.forward(1))  # Should return "page3.com"
    print(browserHistory.back(2))  # Should return "startpage.com"

    # Additional test case 3
    browserHistory = BrowserHistory("initialpage.com")
    print(browserHistory.back(1))  # Should return "initialpage.com" (cannot go back)
    print(browserHistory.forward(1))  # Should return "initialpage.com" (cannot go forward)
    browserHistory.visit("secondpage.com")
    print(browserHistory.back(1))  # Should return "initialpage.com"
    print(browserHistory.forward(1))  # Should return "secondpage.com"


if __name__ == "__main__":
    main()
