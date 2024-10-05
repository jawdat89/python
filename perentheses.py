class Solution:
    def isValid(self, s: str) -> bool:
        _map = {
            '{': '}',
            '[': ']',
            '(': ')'
        }

        stack = []

        for c in s:
            if c in _map:
                stack.append(c)
            else:
                if not stack or _map[stack.pop()] != c:
                    return False
        return not stack
            
        