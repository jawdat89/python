import enum

class GridPosition(enum.Enum):
    EMPTY = 0
    YELLOW = 1
    RED = 2

class Grid:
    def __init__(self, rows: int, cols: int):
        self._rows = rows
        self._cols = cols
        self._grid = None
        self.initGrid()

    # initializes the grid with empty positions
    def initGrid(self) -> None:
        self._grid = [[GridPosition.EMPTY for _ in range(self._cols)] for _ in range(self._rows)]

    # returns the grid
    def getGrid(self) -> list:
        return self._grid
    
    # returns the position of the grid
    def getColumnCount(self) -> int:
        return self._cols
    
    # returns placing a piece in the grid and
    # returns the row where the piece is placed
    # if the column is full, return an error
    def placePiece(self, col: int, piece: GridPosition) -> int:
        if col < 0 or col >= self._cols:
            return ValueError("Invalid column")
        if piece == GridPosition.EMPTY:
            return ValueError("Invalid piece")
        for row in range(self._rows - 1, -1, -1):
            if self._grid[row][col] == GridPosition.EMPTY:
                self._grid[row][col] = piece
                return row
            
        return ValueError("Column is full")
    
    # check if there is a win in the grid
    def checkWin(self, connectN: int, row: int, col:int , piece: GridPosition) -> bool:
        # count = 0
        # # check horizontal
        # for c in range(self._cols):
        #   if self._grid[row][c] == piece:
        #     count += 1
        #   else:
        #     count = 0

        #   if count == connectN:
        #     return True
        
        # count = 0
        # # check vertical
        # for r in range(self._rows):
        #   if self._grid[r][col] == piece:
        #     count += 1
        #   else:
        #     count = 0

        #   if count == connectN:
        #     return True
            
        # count = 0
        # # check diagonal
        # for r in range(self._rows):
        #   c = row + col - r
        #   if c >= 0 and c < self._cols and self._grid[r][c] == piece:
        #     count += 1
        #   else:
        #     count = 0

        #   if count == connectN:
        #     return True
            
        # count = 0
        # # check anti-diagonal
        # for r in range(self._rows):
        #   c = col - row + r
        #   if c >= 0 and c < self._cols and self._grid[r][c] == piece:
        #     count += 1 
        #   else:
        #     count = 0

        #   if count == connectN: 
        #     return True

        directions = [(0, 1), (1, 0), (1, 1), (1, -1)] # right, down, diagonal, anti-diagonal
        for dr, dc in directions:
            count = 1
            for i in range(1, connectN):
                r, c = row + i * dr, col + i * dc
                if min(r, c) < 0 or r >= self._rows or c >= self._cols or self._grid[r][c] != piece:
                    break
                count += 1
            for i in range(1, connectN):
                r, c = row - i * dr, col - i * dc
                if min(r, c) < 0 or r >= self._rows or c >= self._cols or self._grid[r][c] != piece:
                    break
                count += 1
            if count >= connectN:
                return True
          
        # no win
        return False
      
    # check if the grid is full
    def isFull(self) -> bool:
        for row in range(self._rows):
            for col in range(self._cols):
                if self._grid[row][col] == GridPosition.EMPTY:
                    return False
        return True
      
class Player:
    def __init__(self, name: str, pieceColor: GridPosition):
        self._name = name
        self._pieceColor = pieceColor
        
    def getName(self) -> str:
        return self._name
      
    def getPieceColor(self) -> GridPosition:
        return self._pieceColor
      
class Game:
    # grid: the grid for the game
    # connectN: the number of pieces to connect to win
    # targetScore: the score to win the game
    def __init__(self, grid: Grid, connectN: int, targetScore: int):
        self._grid = grid
        self._connectN = connectN
        self._targetScore = targetScore
        
        self._players = [
          Player("Player 1", GridPosition.YELLOW),
          Player("Player 2", GridPosition.RED)
        ]
        
        self.score = {}
        for player in self._players:
            self.score[player.getName()] = 0
            
    def printBoard(self):
        print('Board\n')
        grid = self._grid.getGrid()
        
        for i in range(len(grid)):
            row = ''
            for piece in grid[i]:
                if piece == GridPosition.EMPTY:
                    row += '0 '
                elif piece == GridPosition.YELLOW:
                    row += 'Y '
                else:
                    row += 'R '

            print(row)
        print(' ')

    # play a move for a player 
    # return the row and column where the piece is placed
    def playMove(self, player: Player):
        self.printBoard()
        print(f"{player.getName()}'s turn")
        colCnt  = self._grid.getColumnCount()
        moveColumn = int(input(f"Enter column between {0} and {colCnt - 1} to add piecec: "))
        moveRow = self._grid.placePiece(moveColumn, player.getPieceColor())

        return (moveRow, moveColumn)

    def playRound(self) -> Player:
        while True:
           for player in self._players:
                row, col = self.playMove(player)
                pieceColor = player.getPieceColor()

                if self._grid.checkWin(self._connectN, row, col, pieceColor):
                    self.score[player.getName()] += 1
                    self.printBoard()
                    return player 
                
    def play(self):
        maxScore = 0
        winner = None 
        while maxScore < self._targetScore:
            winner = self.playRound()
            print(f"{winner.getName()} wins this round")
            maxScore = max(maxScore, self.score[winner.getName()])

            self._grid.initGrid()
        print(f"{winner.getName()} wins the game")

# Test
if __name__ == "__main__":
    grid = Grid(6, 7)
    game = Game(grid, 4, 2)
    game.play()
    