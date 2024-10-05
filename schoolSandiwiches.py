# from typing import List

# class ListNode:
#     def __init__(self, val=None):
#         self.val = val
#         self.next = None
#         self.prev = None

# class Solution:
#     def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
#         head = ListNode()
#         tail = ListNode()
#         head.next = tail
#         tail.prev = head

#         for student in students:
#             node = ListNode(student)
#             prev = tail.prev
#             node.next = tail
#             node.prev = prev
#             prev.next = node
#             tail.prev = node
        
#         i = 0
#         while i < len(sandwiches):
#             cur = head.next
#             found = False
#             while cur != tail:
#                 if cur.val == sandwiches[i]:
#                     cur.prev.next = cur.next
#                     cur.next.prev = cur.prev
#                     i += 1
#                     found = True
#                     break
#                 cur = cur.next
#             if not found:
#                 break
        
#         count = 0
#         cur = head.next
#         while cur != tail:
#             count += 1
#             cur = cur.next
        
#         return count

# # Test the Solution class with some test cases
# def main():
#     solution = Solution()
#     print(solution.countStudents([1,1,0,0], [0,1,0,1]))  # Should return 0
#     print(solution.countStudents([1,1,1,0,0,1], [1,0,0,0,1,1]))  # Should return 3

# if __name__ == "__main__":
#     main()

from typing import List
from collections import Counter, deque

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        
        # students_queue = deque(students)
        # sandwiches_stack = sandwiches

        # while students_queue and sandwiches_stack:
        #     student = students_queue.popleft()
        #     if student == sandwiches_stack[0]:
        #         sandwiches_stack.pop(0)
        #     else:
        #         students_queue.append(student)
        #     # If we have gone through the entire queue and made no progress, we are stuck
        #     if all(s != sandwiches_stack[0] for s in students_queue):
        #         break

        # return len(students_queue)

        res = len(students)
        # cnt = {}
        # for s in students:
        #     if s not in cnt:
        #         cnt[s] = 0
        #     cnt[s] += 1
        cnt = Counter(students)

        for s in sandwiches:
            if cnt[s] > 0:
                res -= 1
                cnt[s] -= 1
            else:
                return res


        return res


# Test the Solution class with some test cases
def main():
    solution = Solution()
    print(solution.countStudents([1, 1, 0, 0], [0, 1, 0, 1]))  # Should return 0
    print(solution.countStudents([1, 1, 1, 0, 0, 1], [1, 0, 0, 0, 1, 1]))  # Should return 3

if __name__ == "__main__":
    main()
