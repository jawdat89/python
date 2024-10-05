class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return Counter(s) == Counter(t)


        # for c in s:
        #     if c not in countS:
        #         countS[c] = 0
        #     countS[c] += 1
        # for c in t:
        #     if c not in countT:
        #         countT[c] = 0
        #     countT[c] += 1
        
        # return countS == countT
        if len(s) != len(t):
          return False

        countS = {}
        countT = {}
        for i in range(len(s)):
          countS[s[i]] = 1 + countS.get(s[i], 0) # 0 is default value if key not found
          countT[t[i]] = 1 + countT.get(t[i], 0)
        for c in countS:
          if countS[c] != countT.get(c, 0): # if c not found in countT, return 0
              return False
        return True
        # using Counter similar to above
        return Counter(s) == Counter(t)
        # sorting and comparing
        return sorted(s) == sorted(t)

    
