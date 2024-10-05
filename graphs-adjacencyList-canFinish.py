from typing import List

class Solution:
  def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
      # Create a dictionary to map each course to its list of prerequisites
      preMap = {i: [] for i in range(numCourses)}
      
      # Fill the preMap with the prerequisites for each course
      for crs, pre in prerequisites:
          preMap[crs].append(pre)

      # visitSet keeps track of all courses along the current DFS path
      visitSet = set()

      def dfs(crs):
          # If the course is already in the visitSet, a cycle is detected
          if crs in visitSet:
              return False
          # If the course has no prerequisites, it can be completed
          if preMap[crs] == []:
              return True

          # Add the course to the visitSet
          visitSet.add(crs)
          # Recursively check all prerequisites for the current course
          for pre in preMap[crs]:
              if not dfs(pre):
                  return False

          # Remove the course from the visitSet after visiting
          visitSet.remove(crs)
          # Mark the course as having no prerequisites to avoid reprocessing
          preMap[crs] = []

          return True

      # Check each course to see if it can be completed
      for crs in range(numCourses):
          if not dfs(crs):
              return False
      return True

def test_canFinish():
  solution = Solution()

  # Test Case 1: No prerequisites
  numCourses1 = 2
  prerequisites1 = []
  assert solution.canFinish(numCourses1, prerequisites1) == True
  print("Test Case 1 Passed: No prerequisites")

  # Test Case 2: Simple cycle
  numCourses2 = 2
  prerequisites2 = [[1, 0], [0, 1]]
  assert solution.canFinish(numCourses2, prerequisites2) == False
  print("Test Case 2 Passed: Simple cycle")

  # Test Case 3: Complex graph with no cycle
  numCourses3 = 4
  prerequisites3 = [[1, 0], [2, 1], [3, 2]]
  assert solution.canFinish(numCourses3, prerequisites3) == True
  print("Test Case 3 Passed: Complex graph with no cycle")

# Run the test cases
test_canFinish()