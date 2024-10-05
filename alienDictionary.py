from typing import List

class Solution:
  def foreignDictionary(self, words: List[str]) -> str:
      # Create an adjacency list for each character in the words
      adj = {c: set() for w in words for c in w}

      # Build the graph by comparing adjacent words
      for i in range(len(words) - 1):
          w1, w2 = words[i], words[i + 1]

          # Find the minimum length between the two words
          minLen = min(len(w1), len(w2))

          # Check for invalid order: if w1 is longer than w2 but w1 starts with w2
          if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
              return ""  # Invalid order, return empty string

          # Compare characters of the two words to build the graph
          for j in range(minLen):
              if w1[j] != w2[j]:
                  # Add a directed edge from w1[j] to w2[j]
                  adj[w1[j]].add(w2[j])
                  break  # Only the first different character matters

      # Dictionary to track visited nodes: False=visited, True=visited & current path
      visit = {}
      res = []  # List to store the result (topological order)

      # Depth-first search function to detect cycles and build topological order
      def dfs(c):
          if c in visit:
              return visit[c]  # If True, a cycle is detected

          visit[c] = True  # Mark the node as visited and in the current path
          for nei in adj[c]:
              if dfs(nei):  # If a cycle is detected in the neighbor
                  return True

          visit[c] = False  # Mark the node as visited and not in the current path
          res.append(c)  # Add the character to the result list

      # Perform DFS for each character in the adjacency list
      for c in adj:
          if dfs(c):  # If a cycle is detected, return an empty string
              return ""

      res.reverse()  # Reverse the result list to get the correct order
      return "".join(res)  # Join the characters to form the result string