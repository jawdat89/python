from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)  # Dictionary to map character count tuples to lists of anagrams

        for s in strs:
            # Create a count array for 26 lowercase English letters
            count = [0] * 26

            # Count the frequency of each character in the string
            for c in s:
                count[ord(c) - ord("a")] += 1
            
            # Use the count array as a key by converting it to a tuple
            res[tuple(count)].append(s)

        # Return the grouped anagrams as a list of lists
        return res.values()
    
    # Time complexity: O(N * K) where N is the length of strs and K is the maximum length of a string in strs

        res = defaultdict(list)  # Dictionary to map sorted strings to lists of anagrams

        for s in strs:
            # Sort the string and use it as a key
            sorted_str = ''.join(sorted(s))
            # Append the original string to the list of anagrams for this sorted key
            res[sorted_str].append(s)

        # Return the grouped anagrams as a list of lists
        return list(res.values())
    # Time complexity: O(N * K * log(K)) where N is the length of strs and K is the maximum length of a string in strs




if __name__ == '__main__':
    s = Solution()
    print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    # Expected output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]