
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        def alphaNum(c):
            return (ord('A') <= ord(c) <= ord('Z') or
             ord('a') <= ord(c) <= ord('z') or
             ord('0') <= ord(c) <= ord('9'))

        while l < r:
            while l < r and not alphaNum(s[l]):
                l += 1
            while r > l and not alphaNum(s[r]):
                r -= 1

            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1

        return True        


        #############
        # newStr = ""

        # for c in s:
        #     if c.isalnum():
        #         newStr += c.lower()
        
        # return newStr == newStr[::-1]

        # # Step 1: Filter non-alphanumeric characters
        # filtered_chars = filter(str.isalnum, s)
      
        # # Step 2: Convert to lowercase and join to form the processed string
        # cleaned_string = ''.join(filtered_chars).lower()
      
        # # Step 3: Check if the cleaned string is equal to its reverse
        # return cleaned_string == cleaned_string[::-1]