class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        ROWS, COLS = len(board), len(board[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visit = set()

        def dfs(r, c, i):  
            if i == len(word):
                return True
            if (min(r,c ) < 0 or r == ROWS or c == COLS or
                word[i] != board[r][c] or (r, c) in visit):
                return False

            visit.add((r, c))

            res = None
            for dr, dc in directions:
                res = res or dfs(r + dr, c + dc, i + 1) 

            visit.remove((r, c))

            return res

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False
        
        

